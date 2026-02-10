# 🔐 Network Security ML Pipeline with FastAPI & Docker (End To End MLOPS)

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow)
![DagsHub](https://img.shields.io/badge/DagsHub-231F20?logo=dagshub)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb)

An **end-to-end Machine Learning & MLOps project** for Network Security that includes:
- Automated ML pipeline
- Experiment tracking with **MLflow + DagsHub**
- Prediction API using FastAPI
- Dockerized deployment

---

## 🧠 Project Overview

This project detects malicious or suspicious network activity using a machine learning pipeline.  
It supports:
- Data ingestion → validation → transformation → training
- CSV-based prediction via FAST API
- Experiment tracking using DagsHub
- Containerized deployment using Docker

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" width="42"/>
  <img src="https://avatars.githubusercontent.com/u/73596471?s=200&v=4" width="42"/>
</p>

- **Python 3.10**
- **FastAPI** 
- **Scikit-learn** – Machine Learning
- **MLflow** – Experiment tracking
- **DagsHub** – Remote MLflow backend
- **MongoDB** – Data storage
- **Docker** – Containerization

---

## 📂 Project Structure

```text
netsecurity/
│
├── app.py                     # FastAPI application
├── Dockerfile                 # Docker image definition
├── requirements.txt           # Dependencies
├── setup.py                   # Package setup
│
├── networksecurity/
│   ├── components/            # Data ingestion, validation, transformation
│   ├── pipeline/              # Training pipeline
│   ├── utils/                 # Utility functions
│   ├── constant/              # Constants
│   └── logging/               # Logging module
│
├── Artifacts/                 # ML artifacts
├── prediction_output/         # Prediction results
└── templates/                 # HTML templates
```

## 🚀 Run Locally
```
python -m venv venv
venv\Scripts\activate
```
```Install dependencies
pip install -r requirements.txt
```
```Start FastAPI server
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
## 📊 MLflow & DagsHub Tracking

All experiments are logged using MLflow

Remote tracking is enabled via DagsHub
```
https://dagshub.com/<your-username>/networksecurity.mlflow
```

## 🐳 Docker Usage
```Build Image
docker build -t networksecurity-app .
```
```Run Container
docker run -p 8000:8000 networksecurity-app
```
## 🔐 Environment Variables
```Create a .env file:
MONGODB_URL_KEY=your_mongodb_uri
MLFLOW_TRACKING_URI=https://dagshub.com/<username>/networksecurity.mlflow
MLFLOW_TRACKING_USERNAME=your_dagshub_username
MLFLOW_TRACKING_PASSWORD=your_dagshub_token
```
