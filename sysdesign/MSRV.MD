# Microservices

Microservices architecture is a software design approach that structures an application as a collection of small, loosely coupled services. These services are independently deployable, scalable, and responsible for specific functionalities. Microservices architecture (often shortened to microservices) refers to an architectural style for developing applications. Microservices allow a large application to be separated into smaller independent parts, with each part having its own realm of responsibility. To serve a single user request, a microservices-based application can call on many internal microservices to compose its response.

Containers are a well-suited microservices architecture example, since they let you focus on developing the services without worrying about the dependencies. Modern cloud-native applications are usually built as microservices using containers.


Tools : [Google Microservices Stack](https://cloud.google.com/learn/what-is-microservices-architecture), AWS Containers - [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) and Serverless - [AWS Lambda](https://aws.amazon.com/lambda/). Amazon Microservice Ecosystem [stack](https://aws.amazon.com/microservices/). To learn more about MLOps, go to my notes @[MLOPS](./MLOPS.MD) and @[VERTEX AI](./VERTEXAI.MD).

<img src="img/mss.jpg" width=42%><a> </a><img src="img/ff.png" width=56%>

Microservices are an application architecture style where independent, self-contained programs with a single purpose each can communicate with each other over a network. Typically, these microservices are able to be deployed independently because they have strong separation of responsibilities via a well-defined specification with significant backwards compatibility to avoid sudden dependency breakage. [[source](https://www.fullstackpython.com/microservices.html)]

#### Microservice Example:

We develop a video to mp3 conversion flask web application and learn microservices along the way.

Tech stack: [ Python, Flask, MongoDB, RabbitMQ, MySQL, Docker, Kubernetes (kubectl, minikube, [k9](https://k9scli.io/) ) ]

<img src="img/flask2.png" width=100%>

code : @[microservices](microservices)

```docker
    $ docker --version
    $ kubectl
    $ minkube start

```

AUTH SERVICE with JSON WEB TOKEN (JWT) → ( [code](microservices/auth/server.py) ) & ([mysql_db](https://github.com/florist-notes/linux_d/blob/main/sysdesign/microservices/auth/init.sql)) : ` $ mysql -uroot < init.sql`

```python
import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)

@server.route("/login", methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing credentials", 401

    # check db for username and password
    cur = mysql.connection.cursor()

```

` $ docker build . ` > ` $ k9s` to deploy our [infrastructure code](microservices/auth/manifests) for auth deployment. Do `$ kubectl apply -f -/`

MongoDB & GridFs → [code](microservices/gateway/server.py). GridFs helps us store large files in mongodb.

```python

import os, gridfs, pika, json
from flask import Flask, request, send_file
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util
from bson.objectid import ObjectId

server = Flask(__name__)

mongo_video = PyMongo(server, uri="mongodb://host.minikube.internal:27017/videos")

mongo_mp3 = PyMongo(server, uri="mongodb://host.minikube.internal:27017/mp3s")

fs_videos = gridfs.GridFS(mongo_video.db)
fs_mp3s = gridfs.GridFS(mongo_mp3.db)

```

Architecture Overview (RabbitMQ) → [ [code](microservices/rabbit/manifests) ]   Synchronous & Asynchronous Interservice Communication.



Learning : [Microservices Explained in 5 Minutes](https://youtu.be/lL_j7ilk7rc), [Microservice Architecture and System Design with Python & Kubernetes](https://youtu.be/hmkF77F9TLw), [Python Microservices for Beginners](https://youtu.be/rOpJhKa-Chk), [How to Build a Microservice in Python](https://www.makeuseof.com/python-microservice-how-build/), [Python Microservices With gRPC](https://realpython.com/python-microservices-grpc/), [Python Microservices Web App (with React, Django, Flask) - Full Course](https://youtu.be/0iB5IPoTDts), [Python Microservices Full Course - Event-Driven Architecture with RabbitMQ](https://youtu.be/ddrucr_aAzA), [Microservices with FastAPI – Full Course](https://youtu.be/Cy9fAvsXGZA), [Microservices in Python using Flask Framework | Dockerize and Deploy to Kubernetes with Helm](https://youtu.be/SdTzwYmsgoU), [Automate with Python ](https://youtu.be/PXMJ6FS7llk), [Microservices in Python](https://sonusharma-mnnit.medium.com/building-a-microservice-in-python-ff009da83dac), [Building Microservices: Designing Fine-Grained Systems](https://www.amazon.de/-/en/Sam-Newman/dp/1492034029/), [Mastering Chaos - A Netflix Guide to Microservices](https://youtu.be/CZ3wIuvmHeM).