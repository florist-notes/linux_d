# MLOps : Machine Learning Operations


MLOps stands for Machine Learning Operations. MLOps is a core function of Machine Learning engineering, focused on streamlining the process of taking machine learning models to production, and then maintaining and monitoring them.

<img src="./img/mlp.png" width=100%>


<table style="width:100%" >
<tr>
<th>Service Category</th>

<th>Service Description</th>

<th>Available Implementations
</th>
</tr

<tr>
<th>ML Platform</th>
<td>Provisioned as our opinionated preference for ML workflows running on a highly scalable software infrastructure.</td>
<td>Kubeflow, Kubernetes</td>
</tr>

<tr>
<th>ML Frameworks</th>
<td>Select your machine learning and deep learning framework, toolkit, and libraries.</td>
<td>TensorFlow, PyTorch, Cafee, Keras</td>
</tr>

<tr>
<th>Storage Volumne Management</th>
<td>Choose from software and tools for storage to meet your high performance ML needs.</td>
<td>Local FS, AWS EFS, AWS EBS, Ceph (block and object), Minio, NFS, HDFS</td>
</tr>

<tr>
<th>Container Image Governance</th>
<td>Choose from software and tools that register, secure, and manage the distribution of container images.</td>
<td>AWS ECR, Harbor, GitLab</td>
</tr>

<tr>
<th>Workflow Engine</th>
<td>Provisioned by default to govern scheduling and coordination of jobs.</td>
<td>Argo</td>
</tr>

<tr>
<th>Model Training</th>
<td>Include collaboration tooling and interative model training as part of your template.</td>
<td>JupyterHub, TensorBoard, Argo workflow templates</td>
</tr>

<tr>
<th>Model Serving</th>
<td>Pick the tool to expose trained models to business applications.</td>
<td>Seldon, tf-serving</td>
</tr>

<tr>
<th>Model Validation</th>
<td>Set by default, models will be evaluated against test data as part of your ML pipeline.</td>
<td>Argo workflow templates</td>
</tr>

<tr>
<th>Data Storage Services</th>
<td>Choose from storage options befitting the performance of other ML services.</td>
<td>Mini, AWS S3, MongoDB, Cassandra, HDFS</td>
</tr>

<tr>
<th>Data Preparation and Processing</th>
<td>Select your tooling to manage the data processing ovent of your ML pipeline.</td>
<td>x</td>
</tr>

<tr>
<th>Infrastructure Monitoring</th>
<td>Elect which reporting and dashboarding tool gives you the better optics into your stack performance.</td>
<td>Argo, NATS, workflow application templates</td>
</tr>

<tr>
<th>Model Monitoring</th>
<td>Find and choose the appropriate tool to watch model accuracy over time.</td>
<td>Prometheus, Grafana</td>
</tr>

<tr>
<th>Load Balancing & Ingress</th>
<td>Determine the appropriate tool to expose cluster services broadly to other application services.</td>
<td>Prometheus, Grafana, lsto</td>
</tr>

<tr>
<th>Security</th>
<td>Find the right tooling for you to manage certificates, passwords and secret tuned for RBAC across all hybrid-cloud environments.</td>
<td>ELB,Traefik, Ambassador</td>
</tr>
<tr>
<th>Log Management</th>
<td>Make logging easier by choosing pre-integrated tools for ingest, analysis and reporting.</td>
<td>Okta, Hashicorp Vault, AWS Certificate</td>
</tr>


</table>

<img src="./img/mlops.svg" width=100%>


End-to-end MLOps solution : These are fully managed services that provide developers and data scientists with the ability to build, train, and deploy ML models quickly. The top commercial solutions are:

[Amazon Sagemaker](https://aws.amazon.com/sagemaker/), a suite of tools to build, train, deploy, and monitor machine learning models.

Microsoft Azure MLOps suite:
[Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/) to build, train, and validate reproducible ML pipelines
[Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) to automate ML deployments
[Azure Monitor](https://docs.microsoft.com/en-us/azure/azure-monitor/overview) to track and analyze metrics
[Azure Kubernetes Services](https://azure.microsoft.com/en-us/services/kubernetes-service/) and other additional tools.

Google Cloud MLOps suite:
[Dataflow](https://cloud.google.com/dataflow) to extract, validate, and transform data as well as to evaluate models
[AI Platform Notebook](https://cloud.google.com/ai-platform-notebooks) to develop and train models
Cloud Build to build and test machine learning pipelines
[TFX](https://www.tensorflow.org/tfx) to deploy ML pipelines
[Kubeflow Pipelines](https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/) to arrange ML deployments on top of [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine) (GKE).



## MLOPs tools : [Project Jupyter](https://jupyter.org/), [Nbdev](https://github.com/fastai/nbdev), [Airflow](https://airflow.apache.org/), [Kubeflow](https://www.kubeflow.org/), [MLflow](https://mlflow.org/), [Optuna](https://optuna.org/).

Continuous Integration (CI) is no longer only about testing and validating code and components, but also testing and validating data, data schemas, and models.

Continuous Deployment (CD) is no longer about a single software package or service, but a system (an ML training pipeline) that should automatically deploy another service (model prediction service) or roll back changes from a model.

Continuous Testing (CT) is a new property, unique to ML systems, that’s concerned with automatically retraining and serving the models.

## Large Language Models (LLMOps)


Does training large language models (LLMOps) differ from traditional MLOps?
While many of the concepts of MLOps still apply, there are other considerations when training large language models:

<b>Computational Resources</b>: Training and fine-tuning large language models typically involves performing orders of magnitude more calculations on large data sets. To speed this process up, specialized hardware like GPUs are used for much faster data-parallel operations. Having access to these specialized compute resources becomes essential for both training and deploying large language models. The cost of inference can also make model compression and distillation techniques important.

<b>Transfer Learning</b>: Unlike many traditional ML models that are created or trained from scratch, many large language models start from a foundation model and are fine-tuned with new data to improve performance in a more specific domain. Fine-tuning allows state-of-the-art performance for specific applications using less data and fewer compute resources.

<b>Human Feedback</b>: One of the major improvements in training large language models has come through reinforcement learning from human feedback (RLHF). More generally, since LLM tasks are often very open-ended, human feedback from your application’s end users is often critical for evaluating LLM performance. Integrating this feedback loop within your LLMOps pipelines can often increase the performance of your trained large language model.

<b>Hyperparameter Tuning</b>: In classical ML, hyperparameter tuning often centers around improving accuracy or other metrics. For LLMs, tuning also becomes important for reducing the cost and computational power requirements of training and inference. For example, tweaking batch sizes and learning rates can dramatically change the speed and cost of training. Thus, both classical ML and LLMs benefit from tracking and optimizing the tuning process, but with different emphases.

<b>Performance Metrics</b>: Traditional ML models have very clearly defined performance metrics, such as accuracy, AUC, F1 score, etc. These metrics are fairly straightforward to calculate. When it comes to evaluating LLMs, however, a whole different set of standard metrics and scoring apply — such as bilingual evaluation understudy (BLEU) and Recall-Oriented Understudy for Gisting Evaluation (ROGUE) that require some extra considering when implementing

resources : [ml-ops](https://ml-ops.org/), [gcloud-mlops](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), [three levels of mlops](https://ml-ops.org/content/three-levels-of-ml-software), [state of mlops](https://ml-ops.org/content/state-of-mlops), [landscape.lfai.foundation/](https://landscape.lfai.foundation/), @github/[awesome-prodction-ml](https://github.com/EthicalML/awesome-production-machine-learning), [MLOps Landscape in 2023: Top Tools and Platforms](https://neptune.ai/blog/mlops-tools-platforms-landscape), [A Gentle Introduction to MLOps](https://towardsdatascience.com/a-gentle-introduction-to-mlops-7d64a3e890ff), [google cloud services for mlops](https://towardsdatascience.com/google-cloud-services-for-mlops-d1702cd9930e), book : [Practitioners guide to MLOps: A framework for continuous delivery and automation of machine learning.](https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf), [mlops on vertex ai](https://www.cloudskillsboost.google/course_templates/158), [mlops on gcp](https://github.com/GoogleCloudPlatform/mlops-on-gcp), courses : [Machine Learning Engineering for Production (MLOps) Specialization](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops), [Machine Learning Operations (MLOps): Getting Started](https://www.coursera.org/learn/mlops-fundamentals), [ML Operations with Vertex AI](https://www.youtube.com/watch?v=snUEwsft1wY&list=PLgxF613RsGoUuEjJJxJW2JYyZ8g1qOUou).