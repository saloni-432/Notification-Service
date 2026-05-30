import celery

celery_app = celery.Celery("app", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0", include=["app.task"])
task_routes = {
    "app.tasks.*": {"queue": "email"},
    "app.tasks.dlq.*": {"queue": "dead-letter"}
}
