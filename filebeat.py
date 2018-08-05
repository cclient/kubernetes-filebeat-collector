#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

__author__ = 'Cui Dapeng'
__version__ = '0.1'
__description__ = 'collector kubernetes docker contain json-file and mount path files by filebeat'
__license__ = 'MIT'

import argparse
import subprocess
import json

parser = argparse.ArgumentParser(description='')

parser.add_argument('-c', '--contain_path',
                    type=str,
                    required=False,
                    default='/var/lib/docker/containers/',
                    help='')

parser.add_argument('-d', '--filebeat_conf',
                    type=str,
                    required=False,
                    default='./filebeat.yml',
                    help='default filebeat conf path')

parser.add_argument('-l', '--log_path_mount',
                    type=str,
                    required=False,
                    default='',
                    help='docker run -v /var/dir:/var/log, write log in /var/log, this value is /var/log')

parser.add_argument('-m', '--log_file_match',
                    type=str,
                    required=False,
                    default='*.log',
                    help='*.log')                    

parser.add_argument('-t', '--task',
                    type=str,
                    required=True,
                    default='start',
                    help='stop,start')

parser.add_argument('-p', '--filebeat_home',
                    type=str,
                    required=False,
                    default='/home/cuidapeng/filebeat',
                    help='')


containers_path = '/var/lib/docker/containers/'
default_filebeat_path = './filebeat.yml'
filebeat_home = '/home/cuidapeng/filebeat'
log_path_mount = ''
log_path_mount = '*.log'


def get_config_file(contain_id):
    return containers_path + "/" + contain_id + "/config.v2.json"


def get_runing_filebeat():
    cmd = ["/bin/sh", "-c", "pgrep -a  -f filebeat | grep -v filebeat.py"]
    stat=""
    try:
     stat = subprocess.check_output(cmd)
    except subprocess.CalledProcessError as ex:
        pass
    ps_lines = stat.split("\n")        
    ps_lines = list(filter(lambda ps_line: len(ps_line) > 0, ps_lines))
    fb_infos = list(map(lambda ps_line: ps_line.split(" "), ps_lines))
    fb_infos = list(map(lambda fb_info: {"pid": fb_info[0], "conf": fb_info[
                    -1], "cid": fb_info[-1].split(".")[0].split("_")[-1]}, fb_infos))
    return fb_infos                
    print(fb_infos)


def get_docker_contain():
    cmd = ["/bin/sh", "-c", "ls /var/lib/docker/containers/*/config.v2.json"]
    stat = subprocess.check_output(cmd)
    contain_confs = stat.split("\n")
    contain_infos = []
    for contain_conf in contain_confs:
        if len(contain_conf) == 0:
            continue
        cmd = ["cat", contain_conf]
        stat = subprocess.check_output(cmd)
        contain_info = json.loads(stat)
        # filter k8s contain
        if "io.kubernetes.container.name" not in contain_info["Config"]["Labels"]:
            continue
        simple_contain_info = {
            "id": contain_info["ID"],
            "log_path": contain_info["LogPath"],
            "name": contain_info["Name"],
            "running": contain_info["State"]["Running"],
            "hostname": contain_info["Config"]["Hostname"],
            "io_kubernetes_container_name": contain_info["Config"]["Labels"]["io.kubernetes.container.name"],
            "io_kubernetes_docker_type": contain_info["Config"]["Labels"]["io.kubernetes.docker.type"],
            "io_kubernetes_pod_name": contain_info["Config"]["Labels"]["io.kubernetes.pod.name"],
            "io_kubernetes_pod_namespace": contain_info["Config"]["Labels"]["io.kubernetes.pod.namespace"],
            "io_kubernetes_pod_uid": contain_info["Config"]["Labels"]["io.kubernetes.pod.uid"]
        }
        if len(log_path_mount)>0 and log_path_mount in contain_info["MountPoints"]:
            simple_contain_info["mount_log_path"]=contain_info["MountPoints"][log_path_mount]["Source"]
        # filter k8s.gcr.io/pause
        if simple_contain_info["io_kubernetes_docker_type"] == "podsandbox":
            continue
        # filter kube-system
        if simple_contain_info["io_kubernetes_pod_namespace"] in ["kube-system", "monitoring"]:
            continue
        # filter running         
        if not simple_contain_info["running"]:
            continue            
        contain_infos.append(simple_contain_info)
    return contain_infos


def _kill_filebeat(runing_filebeat):
            cmd = ["kill", runing_filebeat["pid"]]
            stat = subprocess.check_output(cmd)
            print(cmd, runing_filebeat["conf"])

def _stop_filebeat(contain_infos, runing_filebeats):
    for runing_filebeat in runing_filebeats:
        if len(list(filter(lambda contain_info: contain_info["id"] == runing_filebeat["cid"], contain_infos))) == 0:
            _kill_filebeat(runing_filebeat)


def _start_filebeat(contain_infos, runing_filebeats):
    for contain_info in contain_infos:
        need_start_filebeats = []
        if len(list(filter(lambda runing_filebeat: contain_info["id"] == runing_filebeat["cid"], runing_filebeats))) == 0:
            need_start_filebeats.append(contain_info)
            target_filebeat_name = "filebeat_" + \
                contain_info["io_kubernetes_container_name"] + "_" + \
                contain_info["io_kubernetes_pod_name"] + \
                "_" + contain_info["id"]
            target_filebeat_path = target_filebeat_name + ".yml"
            cmd = ["cp", default_filebeat_path, target_filebeat_path]
            stat = subprocess.check_output(cmd)

            cmd = ["/bin/sh", "-c", "sed -i 's/io_kubernetes_container_name/" +
                   contain_info["io_kubernetes_container_name"] + "/' " + target_filebeat_path]
            stat = subprocess.check_output(cmd)

            cmd = ["/bin/sh", "-c", "sed -i 's/io_kubernetes_pod_name/" +
                   contain_info["io_kubernetes_pod_name"] + "/' " + target_filebeat_path]
            stat = subprocess.check_output(cmd)
            
            cmd = ["/bin/sh", "-c", "sed -i 's:docker_logfile_path:" +
                   contain_info["log_path"] + ":' " + target_filebeat_path]
            stat = subprocess.check_output(cmd)

            if "mount_log_path" in contain_info:
               cmd = ["/bin/sh", "-c", "sed -i 's:docker_mount_logfile_path:" +
                   contain_info["mount_log_path"]+"/"+log_file_match + ":' " + target_filebeat_path]
            else:
               cmd = ["/bin/sh", "-c", "sed -i '/docker_mount_logfile_path/d' " + target_filebeat_path]
            stat = subprocess.check_output(cmd)

            cmd = ["/bin/sh", "-c", "nohup " + filebeat_home + "/filebeat -e -c " +
                   target_filebeat_path + " >> " + target_filebeat_name + ".log &"]
            stat = subprocess.check_output(cmd)

def refresh_filebeat():
    runing_filebeats = get_runing_filebeat()
    contain_infos = get_docker_contain()
    _stop_filebeat(contain_infos,runing_filebeats)
    _start_filebeat(contain_infos,runing_filebeats)

def kill_all_filebeat():
    runing_filebeats = get_runing_filebeat()
    for runing_filebeat in runing_filebeats:
            _kill_filebeat(runing_filebeat)

if __name__ == '__main__':
    args = parser.parse_args()
    task = args.task
    if task == 'start':
        containers_path = args.contain_path
        default_filebeat_path = args.filebeat_conf
        filebeat_home = args.filebeat_home
        log_path_mount = args.log_path_mount
        log_file_match = args.log_file_match
        task = args.task
        print(args)
        refresh_filebeat()
    else:
        kill_all_filebeat()
