# Google Cloud : Vertex AI

<img src="./img/vai.png" width=80%>

### MLOps with Vertex AI

@github/[mlops-with-vertexai](https://github.com/GoogleCloudPlatform/mlops-with-vertex-ai), [gcloud-vertexai](https://cloud.google.com/vertex-ai/docs/start/introduction-mlops?hl=de)

```python

from google.cloud import bigquery
from google.cloud import aiplatform as vertex_ai

```
A step by step code guide in jupyter notebook can be found here : [mlops-with-vertex-ai](https://github.com/GoogleCloudPlatform/mlops-with-vertex-ai)

<b>Orchestrate Workflows :</b> Manually training and deploying your models can be time-consuming and error-prone, especially if you have to repeat the processes often.

+ [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines/introduction?hl=de) helps us automate, monitor and control your ML workflows.
  
<b>Track metadata used in your ML system :</b> In data science, it's important to track the parameters, artifacts, and metrics used in your ML workflow, especially if you repeat the workflow often.

+ Vertex [ML Metadata](https://cloud.google.com/vertex-ai/docs/ml-metadata/introduction?hl=de) allows you to record the metadata, parameters, and artifacts used in your ML system. You can then query this metadata to analyze, debug, and audit the performance of your ML system or the artifacts it generates.
  
<b>Identifying the best model for a use case :</b> When trying out new training algorithms, you need to know which trained model performs best.

+ With [Vertex AI Experiments](https://cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments?hl=de), you can track and analyze different model architectures, hyperparameters, and training environments to determine the best model for your use case.

+ With [Vertex AI TensorBoard](https://cloud.google.com/vertex-ai/docs/experiments/tensorboard-overview?hl=de), you can track, visualize, and compare ML tests to measure the performance of your models.

<b>Manage Model Versions :</b> By adding models to a central repository, you can keep track of model versions.

+ [Vertex AI Model Registry](https://cloud.google.com/vertex-ai/docs/model-registry/introduction?hl=de) provides an overview of your models so you can better organize, track, and train new versions. With Model Registry, you can evaluate models, deploy models to an endpoint, create batch predictions, and view details about specific models and model versions.

<b>Manage features :</b> When you reuse ML features across teams, you need a fast and efficient way to share and deploy the features.

+ [Vertex AI Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/overview?hl=de) provides a central repository for organizing, storing, and deploying ML features. By using a central feature store, an organization can reuse ML features at scale and increase the speed of development and deployment of new ML applications.

<b>Monitor model quality :</b> A model deployed to production works best with prediction input data that is similar to the training data. If the input data differs from the data used to train the model, the model's performance can degrade, even if the model itself has not changed.

+ [Vertex AI Model Monitoring](https://cloud.google.com/vertex-ai/docs/model-monitoring?hl=de) monitors models for training-to-deployment and prediction discrepancies, and sends you alerts when the incoming prediction data deviates too far from the training base. You can use the notifications and feature distributions to assess whether you need to retrain your model.

resource: [how we optimised our Vertex AI Pipelines Environments at VMO2 for scale](https://medium.com/@vmo2techteam/the-mlops-cookbook-how-we-optimised-our-vertex-ai-pipelines-environments-at-vmo2-for-scale-ee02ce50d1de), [Practitioners guide to MLOps](https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf?hl=de), [Serverless MLOps with Vertex AI](https://blog.zenml.io/vertex-ai-blog/), class : [Machine Learning Operations With Vertex AI on Google Cloud Platform StatMike](https://www.youtube.com/watch?v=snUEwsft1wY&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou), [Serverless MLOps with Vertex AI and ZenML](https://www.youtube.com/watch?v=qgvmvexGv_c), [Vertex AI Model Garden](https://youtu.be/I7UiSU96CLc), [Google Cloud Tech](https://www.youtube.com/watch?v=I7UiSU96CLc&list=RDCMUCJS9pqu9BzkAMNTmzNMNhvg&index=24), [Google Cloud : Vertex AI](https://www.youtube.com/watch?v=gT4qqHMiEpA&list=PLIivdWyY5sqJ1YuMdGjRwJ3fFYZ_vWQ62), [Vertex AI Pipelines - The Easiest Way to Run ML Pipelines](https://youtu.be/gtVHw5YCRhE), [Learn Vertex AI while building a fraud detection system](https://youtu.be/5kEhkKfs4TI).

