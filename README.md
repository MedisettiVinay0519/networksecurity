# 🔐 Network Security ML Pipeline with FastAPI & Docker

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)](https://www.docker.com/)
[![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow)](https://mlflow.org/)
[![DagsHub](https://img.shields.io/badge/DagsHub-231F20?logo=dagshub)](https://dagshub.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb)](https://www.mongodb.com/)
[![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=github-actions)](https://github.com/features/actions)

An **end-to-end Machine Learning CI pipeline** designed to detect malicious network activities. This project focuses on modular code architecture, automated image building, and remote experiment tracking.

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg" width="42"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg" width="42"/>
  <img src="https://avatars.githubusercontent.com/u/73596471?s=200&v=4" width="42" title="DagsHub"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/github/github-original.svg" width="42"/>
</p>

- **Core:** Python 3.10, FastAPI, Scikit-learn
- **MLOps:** MLflow (Experiment Tracking), DagsHub (Model Registry)
- **Database:** MongoDB Atlas (NoSQL)
- **DevOps:** Docker (Containerization), GitHub Actions (CI Pipeline)

---

## 🏗️ Project Architecture

```mermaid
graph TD
    A[MongoDB Atlas] -->|Data Ingestion| B(Data Validation)
    B --> C(Data Transformation)
    C --> D(Model Trainer)
    D -->|Push Metrics| E[DagsHub/MLflow]
    D -->|Export Artifact| F[Model Serialization]
    F --> G(FastAPI Endpoint)
    G --> H{User Prediction}
    subgraph CI Pipeline
    J[Code Push] --> K[GitHub Actions]
    K --> L[Docker Build]
    L --> M[Container Image]
    end


```
