## work condition

### same value

`spec.spec.containers.name`

`io_kubernetes_container_name`

`grafana alert rule name`

## start

* ###build and run  

  docker build -t my-webhook ./
  
  docker run -d -p 9000:9000 -e host=127.0.0.1 -e port=6379 -e db=3 --name=webhook my-webhook -verbose -hooks=/etc/webhook/hooks.yml -hotreload

* ###direct run

  docker run -d -p 9000:9000 -e host=127.0.0.1 -e port=6379 -e db=3 --name=webhook cuidapeng/webhook:v0.1 -verbose -hooks=/etc/webhook/hooks.yml -hotreload  
  
## test

### kubernetes-init

curl http://127.0.0.1:9000/hooks/kubernetes-init?contain=consume

server log

```log
[webhook] 2018/07/27 05:41:09 [869730] incoming HTTP request from 10.10.3.47:54748
[webhook] 2018/07/27 05:41:09 [869730] kubernetes-init got matched
[webhook] 2018/07/27 05:41:09 [869730] kubernetes-init hook triggered successfully
[webhook] 2018/07/27 05:41:09 [869730] executing /home/webhook/k8s-redis-initContainers.sh (/home/webhook/k8s-redis-initContainers.sh) with arguments ["/home/webhook/k8s-redis-initContainers.sh"] and environment [contain=consume] using  as cwd
[webhook] 2018/07/27 05:41:09 [869730] command output: 0
[webhook] 2018/07/27 05:41:09 [869730] finished handling kubernetes-init
[webhook] 2018/07/27 05:41:09 200 | 4.85749ms | 10.10.3.54:9000 | GET /hooks/kubernetes-init
```

### kubernetes-liveness

curl http://127.0.0.1:9000/hooks/kubernetes-liveness?contain=consume

server log

```log
[webhook] 2018/07/27 05:41:21 [bc0972] incoming HTTP request from 10.10.3.47:55503
[webhook] 2018/07/27 05:41:21 [bc0972] kubernetes-liveness got matched
[webhook] 2018/07/27 05:41:21 [bc0972] kubernetes-liveness hook triggered successfully
[webhook] 2018/07/27 05:41:21 [bc0972] executing /home/webhook/k8s-redis-livenessProbe.sh (/home/webhook/k8s-redis-livenessProbe.sh) with arguments ["/home/webhook/k8s-redis-livenessProbe.sh"] and environment [contain=consume] using  as cwd
[webhook] 2018/07/27 05:41:21 [bc0972] command output: 0
[webhook] 2018/07/27 05:41:21 [bc0972] finished handling kubernetes-liveness
[webhook] 2018/07/27 05:41:21 200 | 4.178519ms | 10.10.3.54:9000 | GET /hooks/kubernetes-liveness
```

--

#### use redis store contain status

#### use [webhook](https://github.com/adnanh/webhook) hook grafana alert,kubernetes status check request,see detail [webhook config](https://github.com/adnanh/webhook/blob/master/docs/Webhook-Parameters.md) 

--

### kubernetes

[ini-containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

curl http://alert_hook_server:9000/kubernetes-init?contai=consume

redis: del consume

[livenessProbe](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#container-probes)

curl http://alert_hook_server:9000/kubernetes-liveness?contai=consume

redis: exists consume

--

### grafana alert

alerting

```alerting
{ evalMatches: [ { value: 1896, metric: 'Count', tags: {} } ],
  ruleId: 1,
  ruleName: 'consume',
  ruleUrl: 'http://localhost:3000/d/Xbu8_nFmz/consume?fullscreen=true&edit=true&tab=alert&panelId=2&orgId=1',
  state: 'alerting',
  title: '[Alerting] consume'
}
```

redis: set consume 1

ok

```ok
{ evalMatches: [],
  ruleId: 1,
  ruleName: 'consume',
  ruleUrl: 'http://localhost:3000/d/Xbu8_nFmz/consume?fullscreen=true&edit=true&tab=alert&panelId=2&orgId=1',
  state: 'ok',
  title: '[OK] consume'
}
```

redis: del consume

--

demo.yml(curl need image [busybox-curl](https://github.com/yauritux/busybox-curl))

```demo
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
        command: ['sh', '-c', 'curl http://alert_hook_server:9000/hooks/kubernetes-init?contain=consume && echo The app is running! && sleep 3600']
        livenessProbe:
           exec:
             command: ['sh', '-c', 'return $(curl -fsSL http://alert_hook_server:9000/hooks/kubernetes-liveness?contain=consume)']
           initialDelaySeconds: 5
           periodSeconds: 5
      initContainers:
      - name: init-myservice
        image: cuidapeng/busybox-curl:v0.1
        command: ['sh', '-c', 'curl http://alert_hook_server:9000/hooks/kubernetes-init?contain=consume;']
```