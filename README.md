# Sentiment Analysis API

A REST API that classifies text as positive or negative and stores every result in a database.

## Tech Stack
FastAPI, Hugging Face Transformers, SQLAlchemy, SQLite, Docker, AWS EC2

## Endpoints
- `GET /`: health check
- `POST /predict`: send text, get sentiment and confidence
- `GET /history`: list past predictions

## Run with Docker
```
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```
Then open http://127.0.0.1:8000/docs

## Deployment
The Docker image is pushed to Docker Hub and runs on an AWS EC2 Ubuntu instance.