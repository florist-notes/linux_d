# Flask : [[documentation](https://flask.palletsprojects.com/en/2.3.x/)]

Rest API with Python and Flask : REST stands for REpresentational State Transfer and is an architectural style used in modern web development. It defines a set or rules/constraints for a web application to send and receive data. REST API stands for Restful API, which allows the integration of applications or interaction with RESTful web services. New : [FastAPI](https://fastapi.tiangolo.com/) and use [POSTMAN](https://www.postman.com/) to test API. We know that there are six commonly used HTTP request methods, which are : `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`.

```python

@app.route('/', methods=['GET'])
@app.route('/', methods=['POST'])
@app.route('/', methods=['DELETE'])
@app.route('/', methods=['PUT'])

```

I have some experience with Flask and did few projects ([example-work](https://twitter.com/florist_notes/status/1640584066608123905)). I recently gave a workshop at AI-Makerspace, Digital Product School, Unternehmer Technische Universität München on flask, maps and ML. Tech Stack : [ Flask, JavaScript, Bootstrap, Mapbox, MongoDB, PyTorch ] and here is the code [repository](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI). 



<img src="img/flask.png" width=100%>


## Flask Template Gallery :

<table style="width:100%" >
<tr>
<th>
  <p>
  <img src="./img/flask-python.png" width=70%>
  <br />Flask (basic)<br />
  
  [code](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI/v1-prototype-basic) ✔️
  </p>

</th>
<th>
  <p>
  <img src="./img/js.png" width=20%>
  <br />Flask (design+js)<br />
  
  [code](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI/v2-aesthetic-design-%26-js) ✔️
  </p>
</th>
<th>

  <p>
  <img src="./img/fb.png" width=15%>
  <br />Flask (input)<br />
  
  [code](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI/v3-input-users) ✔️
  </p></th>
<th>

  <p>
  <img src="./img/mp.png" width=50%>
  <br />Flask (mapbox + mongoDB)<br />
  
  [code](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI/v4-map-mongo) ✔️
  </p>
  </a></th>
</tr>
<tr>
<th>
  <p>
  <img src="./img/cesium.png" width=40%>
  <br />Flask (3dmap - cesium + AR)<br />
  
  [code](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI/v5-3dmap-AR) ✔️
  </p>

</th>
<th>
  <p>
  <img src="./img/tf.png" width=20%>
  <br />Flask (deep learning - tf/pytorch)<br />
  
  [code](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI/v6-ds-deeplearning) ✔️
  </p>
</th>
<th>

  <p>
  <img src="./img/docker.png" width=30%>
  <br />Flask (docker + gcloud)<br />
  
  [code](https://github.com/DigitalProductschool/AI-Makerspace/tree/master/FlaskGeoAI/v7-glcoud-docker) ✔️
  </p></th>
<th>


  </a></th>
</tr>
</table>

Deployment of Flask server : [PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/), [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python), [Digital Ocean](https://docs.digitalocean.com/tutorials/app-deploy-flask-app/), Virtual Machine from Google Cloud : [Google App Engine](https://cloud.google.com/appengine/docs/standard/python3/runtime), [Google Cloud Run](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service), AWS : [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html), Azure [IIS](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python) etc. 

```python

import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print name
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for record in records:
            if record['name'] == name:
                return jsonify(record)
        return jsonify({'error': 'data not found'})

@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)

@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['name'] == record['name']:
            r['email'] = record['email']
        new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)
    
@app.route('/', methods=['DELETE'])
def delte_record():
    record = json.loads(request.data)
    new_records = []
    with open('/tmp/data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['name'] == record['name']:
                continue
            new_records.append(r)
    with open('/tmp/data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)

app.run(debug=True)
```

Resources: [Flask Mega Tutrial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world), [Build a blog platform with Flask: writing and showing posts](https://blog.teclado.com/build-own-blog-platform-flask-python-part-1/), [Flask documentation : a minimal application](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application), [The Ultimate Flask Course](https://www.udemy.com/course/the-ultimate-flask-course/), [REST APIs with Flask and Python](https://www.udemy.com/course/rest-api-flask-and-python/), [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/), [Python REST API Tutorial - Building a Flask REST API](https://youtu.be/GMppyAPbLYk), [Postman API Test Automation](https://youtu.be/zp5Jh2FIpF0).