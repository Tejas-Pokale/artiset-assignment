# 🚀 Base64 Encoder / Decoder

A modern web application for encoding and decoding messages using Base64, built with **FastAPI** and deployed on **Google Cloud Run** via a fully automated **CI/CD pipeline**.

> Developed as part of a DevOps assignment demonstrating end-to-end application development, containerization, and cloud deployment.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Docker](#docker)
- [CI/CD Pipeline](#cicd-pipeline)
- [Cloud Deployment](#cloud-deployment)
- [Security](#security)
- [Assignment Requirements](#assignment-requirements)

---

## Overview

This project demonstrates a complete DevOps lifecycle including:

- Application development using **Python (FastAPI)**
- Containerization using **Docker**
- Automated CI/CD using **GitHub Actions**
- Deployment to a managed cloud platform (**Google Cloud Run**)
- Zero-downtime production deployments
- Strict test enforcement (pipeline fails on warnings or errors)

---

## Architecture

```
Local Development
       ↓
GitHub Repository
       ↓
GitHub Actions CI/CD
  ├── Run tests (strict mode)
  ├── Build Docker image
  └── Push to Artifact Registry
       ↓
Google Cloud Run
  ├── Automatic revision-based deployment
  └── Zero downtime rollout
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python 3.12) |
| Testing | Pytest |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Container Registry | Google Artifact Registry |
| Deployment Platform | Google Cloud Run |
| UI | HTML, CSS, Vanilla JavaScript |

---

## Features

### API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Modern UI for encoding and decoding |
| `POST /encrypt` | Encodes text using Base64 |
| `POST /decrypt` | Decodes Base64 text |
| `GET /health` | Health check endpoint |

### UI Highlights

- Modern glassmorphism design
- Responsive layout
- JavaScript Fetch API (no page reloads)
- Modal dialog for result display

### Deployment Highlights

- Automatic HTTPS via Cloud Run
- Auto-scaling and horizontal scaling support
- Revision-based deployments with zero downtime
- Minimum instances configurable to avoid cold starts

---

## Project Structure

```
fastapi-encoder/
│
├── app/
│   ├── main.py
│   ├── encoder.py
│   ├── templates/
│   │   └── index.html
│   └── __init__.py
│
├── tests/
│   └── test_app.py
│
├── Dockerfile
├── requirements.txt
├── pytest.ini
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- pip

### Run Locally

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the application**

   ```bash
   uvicorn app.main:app --reload
   ```

3. **Visit the app**

   ```
   http://127.0.0.1:8000
   ```

---

## Docker

### Build the image

```bash
docker build -t fastapi-encoder .
```

### Run the container

```bash
docker run -p 8080:8080 fastapi-encoder
```

The Dockerfile follows production-grade best practices:

- Python 3.12 slim base image
- Non-root user execution
- Optimized layer caching
- No development flags
- Port `8080` configured for Cloud Run compatibility

---

## CI/CD Pipeline

The GitHub Actions pipeline triggers on every push to `main` and performs the following steps:

1. Install dependencies
2. Run `pytest` in strict mode (`-W error`) — any warning is treated as a failure
3. Build Docker image tagged with the commit SHA
4. Push image to **Google Artifact Registry**
5. Deploy to **Google Cloud Run**

### Strict Testing Enforcement

```ini
# pytest.ini
[pytest]
filterwarnings = error
```

The pipeline enforces production-grade code discipline by failing immediately on the first test failure or warning.

---

## Cloud Deployment

Deploy manually using the `gcloud` CLI:

```bash
gcloud run deploy SERVICE_NAME \
  --image REGION-docker.pkg.dev/PROJECT_ID/REPO/IMAGE \
  --region REGION \
  --platform managed \
  --allow-unauthenticated
```

### Deployment Strategy

Each push to `main` creates a new Cloud Run **revision**. Traffic automatically shifts to the healthy revision with no service downtime.

---

## Security

- No hardcoded secrets — all credentials managed via GitHub Secrets
- Service account authentication for CI/CD
- Docker container runs as a **non-root user**
- Images tagged with **commit SHA** for full traceability

---

## Assignment Requirements

| Requirement | Status |
|---|---|
| Sample Program | ✅ Completed |
| Deploy on Server | ✅ Google Cloud Run |
| Containerization | ✅ Docker |
| Push to GitHub | ✅ Completed |
| CI Pipeline | ✅ GitHub Actions |
| Image Push | ✅ Artifact Registry |
| Cloud Deployment | ✅ Zero Downtime |
| Documentation | ✅ This README |

---

## 📸 Submission Includes

- GitHub repository link
- CI/CD workflow file (`.github/workflows/deploy.yml`)
- Screenshots of:
  - Successful GitHub Actions run
  - Artifact Registry image
  - Cloud Run deployment
  - Live application

---

## 🎯 Conclusion

This project demonstrates a complete, production-ready DevOps lifecycle — from local development and containerization through continuous integration, automated deployment, and zero-downtime cloud hosting — following modern cloud-native best practices.
