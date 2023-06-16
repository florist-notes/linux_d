# Kubernetes

<img src="img/kb.png" width=100%>


<img src="img/components-of-kubernetes.svg" width=100%>

Install `cubectl` to [command](https://kubernetes.io/docs/reference/kubectl/) master node in Kubernetes [[install](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)].

```docker

    $ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    $ nano kubeconfig.yaml
    $ export KUBECONFIG=kubeconfig.yaml
    $ kubectl get nodes
    $ kubectl cluster-info
    $ kubectl run skk --image=username/imagename:tag --port=8ß (container is created inside pod named 'skk')
    $ kubectl describe pods
    $ kubectl delete pods skk
    
DEPLOYMENT: configure `deployment.yaml`  
    $ kubectl apply -f deployment.yaml
    $ kubectl get pods
    $ kubectl get deployments
    $ kubectl edit deployment skk-deployment              ( change to 'replica: 10' for 10 pods)
    $ kubectl get pods -o wide

To expose pods to internet we use 'service':

LOAD BALANCER based on label:
    $ kubectl apply -f skk-service.yaml

```
Videos : [Kubernetes Explained in 100 Seconds](https://youtu.be/PziYflu8cB8), [Kubernetes Course - Full Beginners Tutorial (Containerize Your Apps!)](https://youtu.be/d6WC5n9G_sM), [Kubernetes Design Principles: Understand the Why - Saad Ali, Google](https://youtu.be/ZuIQurh_kDk), [you should be using PODMAN](https://youtu.be/0jhdCcAc8nM)