# w2ohw

The code for W2O's "Take Home Challenge to be completed by Candidate"

## Requirement
See file "w2oGroup- DevOps Test and Itinerary.pdf"

## Docker image
https://hub.docker.com/r/yanmingxiao/docker.test


## Finish timestamp on a local K8S cluster

2020-04-13 21-21-29

See the timestamp on the Title bar of the file
 	"Screenshot-from-2020-04-13-21-21-29.png"


![Finish timestamp](Screenshot-from-2020-04-13-21-21-29.png)




## Finish timestamp on an AWS EKS cluster

```shell
EKS node w2oGroup

https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html

eksctl create nodegroup \
--cluster default \
--version auto \
--name standard-workers \
--node-type t3.medium \
--node-ami auto \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4



$ pwd
/home/yxiao/Documents/LEARNING/AWS/ECS_Fargate_EKS/W2Oa


eksctl create nodegroup \
--cluster w2o02 \
--version auto \
--name standard-workers \
--node-type t3.medium \
--node-ami auto \
--nodes 3 \
--nodes-min 1 \
--nodes-max 4



$ eksctl create nodegroup --cluster w2o02 --version auto --name standard-workers --node-type t3.medium --node-ami auto --nodes 3 --nodes-min 1 --nodes-max 4
[ℹ]  eksctl version 0.16.0
[ℹ]  using region us-east-1
[ℹ]  will use version 1.15 for new nodegroup(s) based on control plane version
[ℹ]  nodegroup "standard-workers" will use "ami-0e5bb2367e692b807" [AmazonLinux2/1.15]
[ℹ]  1 nodegroup (standard-workers) was included (based on the include/exclude rules)
[ℹ]  will create a CloudFormation stack for each of 1 nodegroups in cluster "w2o02"
[ℹ]  2 sequential tasks: { fix cluster compatibility, 1 task: { 1 task: { create nodegroup "standard-workers" } } }
[ℹ]  checking cluster stack for missing resources
[ℹ]  cluster stack is missing resources for Fargate
[ℹ]  adding missing resources to cluster stack
[ℹ]  re-building cluster stack "eksctl-w2o02-cluster"
[✔]  all resources in cluster stack "eksctl-w2o02-cluster" are up-to-date
[ℹ]  building nodegroup stack "eksctl-w2o02-nodegroup-standard-workers"
[ℹ]  deploying stack "eksctl-w2o02-nodegroup-standard-workers"
[ℹ]  adding identity "arn:aws:iam::965031037346:role/eksctl-w2o02-nodegroup-standard-w-NodeInstanceRole-17VZBHBB6EOMS" to auth ConfigMap
[ℹ]  nodegroup "standard-workers" has 0 node(s)
[ℹ]  waiting for at least 1 node(s) to become ready in "standard-workers"
[ℹ]  nodegroup "standard-workers" has 3 node(s)
[ℹ]  node "ip-192-168-5-105.ec2.internal" is not ready
[ℹ]  node "ip-192-168-5-90.ec2.internal" is not ready
[ℹ]  node "ip-192-168-53-41.ec2.internal" is ready
[✔]  created 1 nodegroup(s) in cluster "w2o02"
[✔]  created 0 managed nodegroup(s) in cluster "w2o02"
[ℹ]  checking security group configuration for all nodegroups
[ℹ]  all nodegroups have up-to-date configuration

$ kubectl get nodes
NAME                            STATUS   ROLES    AGE   VERSION
ip-192-168-5-105.ec2.internal   Ready    <none>   59s   v1.15.10-eks-bac369
ip-192-168-5-90.ec2.internal    Ready    <none>   61s   v1.15.10-eks-bac369
ip-192-168-53-41.ec2.internal   Ready    <none>   62s   v1.15.10-eks-bac369
$ kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.100.0.1   <none>        443/TCP   53m


$ kubectl create deployment dockertest --image=docker.io/yanmingxiao/docker.test:3.0
deployment.apps/dockertest created

$ kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
dockertest   0/1     1            0           19s

$ kubectl get deployments
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
dockertest   1/1     1            1           2m25s

$ kubectl expose deployment dockertest --type=LoadBalancer --port=8080 --target-port=5000
service/dockertest exposed

$ kubectl get svc
NAME         TYPE           CLUSTER-IP       EXTERNAL-IP                                                              PORT(S)          AGE
dockertest   LoadBalancer   10.100.232.115   a92b4e69359814b1f9db546b1c680734-308891860.us-east-1.elb.amazonaws.com   8080:31706/TCP   10s
kubernetes   ClusterIP      10.100.0.1       <none>                                                                   443/TCP          61m


$ date
Mon Apr 13 23:18:30 EDT 2020

```

![Finish timestamp](AWS-deployment.png)

