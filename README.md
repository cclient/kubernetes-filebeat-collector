collect docker logs attach some simple kubernetes info as kubernetes contain log

## work

* 1 scan docker contains path(default /var/lib/docker/containers) get docker [contain log] and [contain config]

* 2 cp filebeat.yml and modify

* 3 start filebeat

see why&how

--

### k8s start

#### docker build(modify filebeat.yml "localhost:9200" to your es)

docker build -t filebeat_k8s:v0.1 ./

kubectl apply -f deploy-filebeat.yml

### local start

python filebeat.py -l /etc/hosts -m *.log -t start

### local stop

python filebeat.py -t stop

--

$ pgrep -a  -f filebeat

14912 filebeat -e -c filebeat_consume_consume-577cd986c7-8mk4h_caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f.yml

filebeat process info:

```finfo
{
"pid": "14912",
"conf": "filebeat_consume_consume-577cd986c7-8mk4h_caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f.yml",
"cid": "caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f"
}
```

docker contain simple info:

```cinfo
{
    "io_kubernetes_docker_type": "container",
    "io_kubernetes_pod_namespace": "defalt",
    "hostname": "consume-577cd986c7-8mk4h",
    "io_kubernetes_pod_name": "consume-577cd986c7-8mk4h",
    "id": "caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f",
    "io_kubernetes_container_name": "consume"
}
```

filebeat_[io_kubernetes_container_name]_[io_kubernetes_pod_name]_[id].yml

filebeat_consume_consume-577cd986c7-8mk4h_caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f.yml

orgi filebeat.yml

```orgi
filebeat.inputs:
- type: log
    - docker_logfile_path
    - docker_mount_logfile_path
  fields:
    namespace: "default"
    name: "io_kubernetes_container_name"
    pod_name: "io_kubernetes_pod_name"
output.elasticsearch:
  hosts: ["localhost:9200"]
setup.kibana:
  host: "localhost:5601"
```

filebeat_consume_consume-577cd986c7-8mk4h_caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f.yml

```desc
filebeat.inputs:
- type: log
  paths:
    - /var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f-json.log
    - /var/lib/kubelet/pods/444e5054-8eec-11e8-b709-f01fafd51338/etc-hosts/*.log
  fields:
    namespace: "default"
    name: "consume"
    pod_name: "consume-577cd986c7-8mk4h"
output.elasticsearch:
  hosts: ["localhost:9200"]
setup.kibana:
  host: "localhost:5601"
```  

log demo

```demo
{
    "_index": "filebeat-6.3.0-2018.07.25",
    "_type": "doc",
    "_id": "mOeJ0GQBE8FuUBDGk_Sj",
    "_version": 1,
    "_score": null,
    "_source": {
        "@timestamp": "2018-07-25T08:23:53.531Z",
        "source": "/var/lib/docker/containers/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f/caed8938198152778e3715f4bd3c00795f40c812d2cdb87dadfe8b0bb058390f-json.log",
        "offset": 347825,
        "message": "{\"log\":\"exist /tmp/download/20180725_16:12:08.zip true\\n\",\"stream\":\"stdout\",\"time\":\"2018-07-25T08:23:47.947640042Z\"}",
        "input": {
            "type": "log"
        },
        "fields": {
            "pod_name": "consume-577cd986c7-8mk4h",
            "namespace": "default",
            "name": "consume"
        },
        "prospector": {
            "type": "log"
        },
        "beat": {
            "name": "host0",
            "hostname": "host0",
            "version": "6.3.0"
        },
        "host": {
            "name": "host0"
        }
    },
    "fields": {
        "@timestamp": [
            "2018-07-25T08:23:53.531Z"
        ]
    },
    "highlight": {
        "fields.name": [
            "@kibana-highlighted-field@consume@/kibana-highlighted-field@"
        ]
    },
    "sort": [
        1532507033531
    ]
}
```

yaml demo

```k8s
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: consume
  namespace: default
  labels:
    app: consume
spec:
  replicas: 1
  template:
    metadata:
      labels:
        app: consume
    spec:
      containers:
      - name: consume
        imagePullPolicy: Always
        image: cuidapeng/busybox-curl:v0.1
        command: ['sh', '-c', 'echo The app is running! && sleep 3600']
```

spec.spec.containers.name=io_kubernetes_container_name

set `python filebeat.py -l /etc/hosts -m *.log -t start` as cron job
