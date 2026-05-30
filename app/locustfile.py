from locust import HttpUser, task, between

class NotificationUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def send_notification(self):
        self.client.get("/notify/testuser")