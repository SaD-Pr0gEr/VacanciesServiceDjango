import os
from django.core.mail import send_mail
from dotenv import load_dotenv
from loguru import logger


load_dotenv()


def hello_user(user_email):
    try:
        send = send_mail(
            "Hello",
            'HELLO!',
            os.getenv('EMAIL_HOST_USER'),
            [user_email, ]
        )
        if not send:
            logger.warning("Message did'nt send")
        return send
    except Exception as e:
        logger.error(e)
        return
