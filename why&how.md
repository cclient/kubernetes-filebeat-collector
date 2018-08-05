$ kb get pods

NAME                                     READY     STATUS    RESTARTS   AGE

consume-577cd986c7-8mk4h                 1/1       Running   0          3d

$ docker ps |grep consume

`caed89381981    cuidapeng/consume@sha256:483cd48b4b1e2ca53846f11fe953695bcceea59542b77f09044d30644cf3235f  "/app/app"  3 days ago  Up 31 hours k8s_consume_consume-577cd986c7-8mk4h_default_00bea8a1-8bfc-11e8-b709-f01fafd51338_0`

`fda1d939f5b4    k8s.gcr.io/pause:3.1    "/pause"    3 days ago  Up 3 daysk8s_POD_consume-577cd986c7-8mk4h_default_00bea8a1-8bfc-11e8-b709-f01fafd51338_0`

docker contain id:caed89381981

$ ls -alh /var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f

```res
total 2.0M
drwx------  3 root root 4.0K Jul 25 16:10 .
drwxrw-rw- 54 root root  12K Jul 25 15:36 ..
-rw-r-----  1 root root 2.0M Jul 25 17:18 caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f-json.log
drwx------  2 root root 4.0K Jul 20 17:05 checkpoints
-rw-r--r--  1 root root 5.9K Jul 25 16:10 config.v2.json
-rw-r--r--  1 root root 1.9K Jul 25 16:10 hostconfig.json
```

$ cat /var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f/config.v2.json

```config
{
    "StreamConfig": {},
    "State": {
        "Running": true,
        "Paused": false,
        "Restarting": false,
        "OOMKilled": false,
        "RemovalInProgress": false,
        "Dead": false,
        "Pid": 15201,
        "ExitCode": 0,
        "Error": "",
        "StartedAt": "2018-07-23T00:51:31.821704515Z",
        "FinishedAt": "2018-07-23T00:51:31.573484432Z",
        "Health": null
    },
    "ID": "caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f",
    "Created": "2018-07-20T09:05:21.881001304Z",
    "Managed": false,
    "Path": "/app/app",
    "Args": [],
    "Config": {
        "Hostname": "consume-577cd986c7-8mk4h",
        "Domainname": "",
        "User": "0",
        "AttachStdin": false,
        "AttachStdout": false,
        "AttachStderr": false,
        "Tty": false,
        "OpenStdin": false,
        "StdinOnce": false,
        "Env": [
            "KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443",
            "TUICE_PERSONAL_WECHAT_PORT_8883_TCP_PORT=8883",
            "KUBERNETES_SERVICE_HOST=10.96.0.1",
            "KUBERNETES_PORT=tcp://10.96.0.1:443",
            "TUICE_PERSONAL_WECHAT_PORT=tcp://10.109.89.240:8883",
            "TUICE_PERSONAL_WECHAT_PORT_8883_TCP=tcp://10.109.89.240:8883",
            "KUBERNETES_SERVICE_PORT=443",
            "KUBERNETES_SERVICE_PORT_HTTPS=443",
            "KUBERNETES_PORT_443_TCP_PORT=443",
            "KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1",
            "TUICE_PERSONAL_WECHAT_PORT_8883_TCP_ADDR=10.109.89.240",
            "KUBERNETES_PORT_443_TCP_PROTO=tcp",
            "TUICE_PERSONAL_WECHAT_SERVICE_HOST=10.109.89.240",
            "TUICE_PERSONAL_WECHAT_SERVICE_PORT=8883",
            "TUICE_PERSONAL_WECHAT_SERVICE_PORT_SERVER=8883",
            "TUICE_PERSONAL_WECHAT_PORT_8883_TCP_PROTO=tcp",
            "PATH=/go/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
            "GOLANG_VERSION=1.8",
            "GOLANG_SRC_URL=https://golang.org/dl/go1.8.src.tar.gz",
            "GOLANG_SRC_SHA256=406865f587b44be7092f206d73fc1de252600b79b3cacc587b74b5ef5c623596",
            "GOPATH=/app",
            "RUN=pro"
        ],
        "Cmd": null,
        "Healthcheck": {
            "Test": [
                "NONE"
            ]
        },
        "Image": "cuidapeng/consume@sha256:483cd48b4b1e2ca53846f11fe953695bcceea59542b77f09044d30644cf3235f",
        "Volumes": null,
        "WorkingDir": "/app",
        "Entrypoint": [
            "/app/app"
        ],
        "OnBuild": null,
        "Labels": {
            "annotation.io.kubernetes.container.hash": "e1a52ef6",
            "annotation.io.kubernetes.container.restartCount": "0",
            "annotation.io.kubernetes.container.terminationMessagePath": "/dev/termination-log",
            "annotation.io.kubernetes.container.terminationMessagePolicy": "File",
            "annotation.io.kubernetes.pod.terminationGracePeriod": "30",
            "io.kubernetes.container.logpath": "/var/log/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/consume/0.log",
            "io.kubernetes.container.name": "consume",
            "io.kubernetes.docker.type": "container",
            "io.kubernetes.pod.name": "consume-577cd986c7-8mk4h",
            "io.kubernetes.pod.namespace": "default",
            "io.kubernetes.pod.uid": "00bea8a1-8bfc-11e8-b709-f01fafd51338",
            "io.kubernetes.sandbox.id": "fda1d939f5b41e31ca5c5214b4d78b38691d438eeb52d22d4460d49a2a820c1f"
        }
    },
    "Image": "sha256:85c9ca987b6fd310ce1019c28031b670da4d6705e70f1807f17727d48aa4aef4",
    "NetworkSettings": {
        "Bridge": "",
        "SandboxID": "",
        "HairpinMode": false,
        "LinkLocalIPv6Address": "",
        "LinkLocalIPv6PrefixLen": 0,
        "Networks": null,
        "Service": null,
        "Ports": null,
        "SandboxKey": "",
        "SecondaryIPAddresses": null,
        "SecondaryIPv6Addresses": null,
        "IsAnonymousEndpoint": false,
        "HasSwarmEndpoint": false
    },
    "LogPath": "/var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f-json.log",
    "Name": "/k8s_consume_consume-577cd986c7-8mk4h_default_00bea8a1-8bfc-11e8-b709-f01fafd51338_0",
    "Driver": "overlay",
    "MountLabel": "",
    "ProcessLabel": "",
    "RestartCount": 0,
    "HasBeenStartedBefore": true,
    "HasBeenManuallyStopped": false,
    "MountPoints": {
        "/app/conf": {
            "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~configmap/conf",
            "Destination": "/app/conf",
            "RW": false,
            "Name": "",
            "Driver": "",
            "Type": "bind",
            "Relabel": "ro",
            "Propagation": "rprivate",
            "Spec": {
                "Type": "bind",
                "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~configmap/conf",
                "Target": "/app/conf",
                "ReadOnly": true
            }
        },
        "/dev/termination-log": {
            "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/containers/consume/fc3f9ebf",
            "Destination": "/dev/termination-log",
            "RW": true,
            "Name": "",
            "Driver": "",
            "Type": "bind",
            "Propagation": "rprivate",
            "Spec": {
                "Type": "bind",
                "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/containers/consume/fc3f9ebf",
                "Target": "/dev/termination-log"
            }
        },
        "/etc/hosts": {
            "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/etc-hosts",
            "Destination": "/etc/hosts",
            "RW": true,
            "Name": "",
            "Driver": "",
            "Type": "bind",
            "Propagation": "rprivate",
            "Spec": {
                "Type": "bind",
                "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/etc-hosts",
                "Target": "/etc/hosts"
            }
        },
        "/var/log/contain": {
            "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3",
            "Destination": "/var/log/contain",
            "RW": true,
            "Name": "",
            "Driver": "",
            "Type": "bind",
            "Propagation": "rprivate",
            "Spec": {
                "Type": "bind",
                "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3",
                "Target": "/var/log/contain"
            }
        },
        "/tmp/nbbsdownload": {
            "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3-6",
            "Destination": "/tmp/nbbsdownload",
            "RW": true,
            "Name": "",
            "Driver": "",
            "Type": "bind",
            "Propagation": "rprivate",
            "Spec": {
                "Type": "bind",
                "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3-6",
                "Target": "/tmp/nbbsdownload"
            }
        },
        "/var/run/secrets/kubernetes.io/serviceaccount": {
            "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~secret/default-token-g6gr9",
            "Destination": "/var/run/secrets/kubernetes.io/serviceaccount",
            "RW": false,
            "Name": "",
            "Driver": "",
            "Type": "bind",
            "Relabel": "ro",
            "Propagation": "rprivate",
            "Spec": {
                "Type": "bind",
                "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~secret/default-token-g6gr9",
                "Target": "/var/run/secrets/kubernetes.io/serviceaccount",
                "ReadOnly": true
            }
        }
    },
    "SecretReferences": null,
    "AppArmorProfile": "",
    "HostnamePath": "/var/lib/docker/containers/fda1d939f5b41e31ca5c5214b4d78b38691d438eeb52d22d4460d49a2a820c1f/hostname",
    "HostsPath": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/etc-hosts",
    "ShmPath": "/var/lib/docker/containers/fda1d939f5b41e31ca5c5214b4d78b38691d438eeb52d22d4460d49a2a820c1f/shm",
    "ResolvConfPath": "/var/lib/docker/containers/fda1d939f5b41e31ca5c5214b4d78b38691d438eeb52d22d4460d49a2a820c1f/resolv.conf",
    "SeccompProfile": "unconfined",
    "NoNewPrivileges": false
}
```

```label
{
            "annotation.io.kubernetes.container.hash": "e1a52ef6",
            "annotation.io.kubernetes.container.restartCount": "0",
            "annotation.io.kubernetes.container.terminationMessagePath": "/dev/termination-log",
            "annotation.io.kubernetes.container.terminationMessagePolicy": "File",
            "annotation.io.kubernetes.pod.terminationGracePeriod": "30",
            "io.kubernetes.container.logpath": "/var/log/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/consume/0.log",
            "io.kubernetes.container.name": "consume",
            "io.kubernetes.docker.type": "container",
            "io.kubernetes.pod.name": "consume-577cd986c7-8mk4h",
            "io.kubernetes.pod.namespace": "default",
            "io.kubernetes.pod.uid": "00bea8a1-8bfc-11e8-b709-f01fafd51338",
            "io.kubernetes.sandbox.id": "fda1d939f5b41e31ca5c5214b4d78b38691d438eeb52d22d4460d49a2a820c1f"
}
```

$ ls -alh /var/log/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/consume/0.log

lrwxrwxrwx 1 root root 165 Jul 20 17:05 /var/log/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/consume/0.log -> /var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f-json.log

(docker local json.log)+(docker local config.v2.json)=(k8s deploy log)

docker out log 

```desc
filebeat.inputs:
- type: log
  paths:
    - /var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f-json.log
  fields:
    namespace: "default"
    name: "consume"
    pod_name: "consume-577cd986c7-8mk4h"
output.elasticsearch:
  hosts: ["localhost:9200"]
setup.kibana:
  host: "localhost:5601"
```

mount

```mp
{
        "/var/log/contain": {
            "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3",
            "Destination": "/var/log/contain",
            "RW": true,
            "Name": "",
            "Driver": "",
            "Type": "bind",
            "Propagation": "rprivate",
            "Spec": {
                "Type": "bind",
                "Source": "/var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3",
                "Target": "/var/log/contain"
            }
        }
}
```

mount path log(filebeat don't supply all k8s volume,or need do some other work,i just test local and hostPath,i guess nfs should work)

```desc
filebeat.inputs:
- type: log
  paths:
    - /var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3/*
  fields:
    namespace: "default"
    name: "consume"
    pod_name: "consume-577cd986c7-8mk4h"
output.elasticsearch:
  hosts: ["localhost:9200"]
setup.kibana:
  host: "localhost:5601"
```

```all
filebeat.inputs:
- type: log
  paths:
    - /var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f-json.log
    - /var/lib/kubelet/pods/00bea8a1-8bfc-11e8-b709-f01fafd51338/volumes/kubernetes.io~local-volume/pv-3/*
  fields:
    namespace: "default"
    name: "consume"
    pod_name: "consume-577cd986c7-8mk4h"
output.elasticsearch:
  hosts: ["localhost:9200"]
setup.kibana:
  host: "localhost:5601"
```
