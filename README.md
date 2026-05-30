# FastAPI Background Job System

A distributed background job system built with FastAPI, Celery, Redis and MailHog.

## 🔗 Links

* **GitHub:** https://github.com/saloni-432/Notification-Service

## Features

* Asynchronous email queue with Celery
* Redis broker & result backend
* FastAPI integration
* SMTP email delivery using MailHog
* Retry logic for failed jobs
* Dead Letter Queue (DLQ) concept
* Load testing with Locust
* Background task processing
* Fault-tolerant job execution

## Run locally

Start Redis:

```bash
docker run -d -p 6379:6379 redis
```

Start MailHog:

```bash
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
```

Run FastAPI:

```bash
uvicorn app.main:app --reload
```

Start Celery worker:

```bash
celery -A app.celery_app worker --pool=solo --loglevel=info
```

Open:

```text
http://localhost:8000/docs
```

MailHog UI:

```text
http://localhost:8025
```

## 🚀 Endpoints

| Method | Endpoint         | Description                   |
| ------ | ---------------- | ----------------------------- |
| GET    | `/notify/{name}` | Queue email notification task |

## Example Workflow

```text
FastAPI API
    ↓
Celery Task Queue
    ↓
Redis Broker
    ↓
Celery Worker
    ↓
MailHog SMTP
    ↓
Email Delivery
```

## Load Testing

Run Locust:

```bash
locust -f locust.py
```

Open:

```text
http://localhost:8089
```

## Retry Testing

To simulate failures:

```python
SMTP_PORT = 9999
```

Expected behavior:

* Task failure
* Automatic retries
* Retry delay handling
* DLQ concept trigger after failures
