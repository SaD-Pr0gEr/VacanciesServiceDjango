from accounts.email_senders import hello_user
from vacansies_service.celery import app


@app.task
def hello_sender(user_email):
    send = hello_user(user_email)
    return send
