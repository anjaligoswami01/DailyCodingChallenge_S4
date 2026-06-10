# Day 36/60 – Deploy Your AI Backend to the Cloud

## Overview

This project demonstrates deployment of a FastAPI AI backend using Docker and Railway.

## Tech Stack

* Python
* FastAPI
* Docker
* Railway
* GitHub

## Features

* REST API with FastAPI
* Health Check Endpoint
* Environment Variable Configuration
* Dockerized Deployment
* Railway Cloud Hosting
* Automated Redeployment

## API Endpoints

### Root

```http
GET /
```

### Health Check

```http
GET /health
```

### Query Endpoint

```http
POST /query
```

Request:

```json
{
  "question": "Hello"
}
```

Response:

```json
{
  "question": "Hello",
  "model": "gpt-4",
  "threshold": 0.75,
  "answer": "Processed: Hello"
}
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Run with Docker

```bash
docker build -t ai-backend .
docker run -p 8000:8000 ai-backend
```

## Learning Outcomes

* Containerized a FastAPI application
* Built Docker images
* Managed environment variables
* Prepared application for cloud deployment
* Implemented health monitoring endpoint
