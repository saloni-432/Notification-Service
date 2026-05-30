from app.celery_app import celery_app
from email.message import EmailMessage
from smtplib import SMTP, SMTPException

SMTP_HOST = "localhost"
SMTP_PORT = 1025
FROM_EMAIL = "sender@example.com"


@celery_app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=5
)
def send_notification(self, name):
    try:
        print("Task started")

        msg = EmailMessage()
        msg["Subject"] = "Notification"
        msg["From"] = FROM_EMAIL
        msg["To"] = f"{name}@example.com"
        msg.set_content(f"Hello {name}")

        print("Sending email...")

        with SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as smtp:
            smtp.send_message(msg)

        print("Email sent successfully")

    except (SMTPException, ConnectionError) as exc:
        print("Failure → retrying")
        raise self.retry(exc=exc)

    except Exception as exc:
        # DEAD LETTER QUEUE concept
        print("Sending to DLQ")
        self.send_to_dlq(name, str(exc))
        raise

def send_to_dlq(name, error):
    print(f"DLQ: {name} failed → {error}")