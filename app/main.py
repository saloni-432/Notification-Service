from fastapi import FastAPI, BackgroundTasks
from time import sleep
from app.task import send_notification

app = FastAPI()

@app.get("/notify/{name}")
def read_notify(name: str):
    task=send_notification.delay(name)
    return {"message": "queued", "task_id": task.id}

