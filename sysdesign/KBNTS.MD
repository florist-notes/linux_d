# Kubernetes

<img src="img/kb.png" width=100%>

Kubernetes, often abbreviated as K8s, is an open-source platform designed to manage and orchestrate containerized applications across a cluster of computers. Imagine you have several applications that need to run across many computers (or servers), each wrapped in its own container (a lightweight package that includes the application and everything it needs to run). Kubernetes is like the conductor of an orchestra, ensuring that all these containers work together smoothly, are always running where they should be, and can be easily scaled up or down based on demand.


<img src="img/components-of-kubernetes.svg" width=100%>

+ `Pods`: The smallest and simplest Kubernetes object. A pod usually runs a single container.
+ `Nodes`: The machines (physical or virtual) that run your applications.
+ `Clusters`: A set of nodes managed by Kubernetes.
+ `Services`: Define how to access the application running in your pods.
+ `Deployments`: Help manage your application by defining the number of replicas (copies) and updates.

Start small by deploying a simple application. Write a configuration file (usually in YAML format) that tells Kubernetes what to do, then use the `kubectl` command-line tool to apply it.

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

## k9s : Kubernetes CLI To Manage Your Clusters In Style! [web](https://k9scli.io/) | [github](https://github.com/derailed/k9s/tree/master)

<img src="img/k9s.png" width=100%>


## The Command Line

```shell
# List all available CLI options
k9s help
# To get info about K9s runtime (logs, configs, etc..)
k9s info
# To run K9s in a given namespace
k9s -n mycoolns
# Start K9s in an existing KubeConfig context
k9s --context coolCtx
# Start K9s in readonly mode - with all cluster modification commands disabled
k9s --readonly
```

## Logs

Given the nature of the ui k9s does produce logs to a specific location. To view the logs and turn on debug mode, use the following commands:

```shell
k9s info
# Will produces something like this
#  ____  __.________
# |    |/ _/   __   \______
# |      < \____    /  ___/
# |    |  \   /    /\___ \
# |____|__ \ /____//____  >
#         \/            \/
#
# Configuration:   ~/Library/Preferences/k9s/config.yml
# Logs:            /var/folders/8c/hh6rqbgs5nx_c_8k9_17ghfh0000gn/T/k9s-fernand.log
# Screen Dumps:    /var/folders/8c/hh6rqbgs5nx_c_8k9_17ghfh0000gn/T/k9s-screens-fernand

# To view k9s logs
tail -f /var/folders/8c/hh6rqbgs5nx_c_8k9_17ghfh0000gn/T/k9s-fernand.log

# Start K9s in debug mode
k9s -l debug
```


Videos : [Kubernetes Explained in 100 Seconds](https://youtu.be/PziYflu8cB8), [Kubernetes Course - Full Beginners Tutorial (Containerize Your Apps!)](https://youtu.be/d6WC5n9G_sM), [Kubernetes Design Principles: Understand the Why - Saad Ali, Google](https://youtu.be/ZuIQurh_kDk), [you should be using PODMAN](https://youtu.be/0jhdCcAc8nM)