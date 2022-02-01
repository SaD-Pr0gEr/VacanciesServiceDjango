import os
from django.core.mail import send_mail
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
    

def help_sender(name, email, text):
    mail_text = f'Пользователь с именем {name} отправил заявку с вопросом!\n Вот текст вопроса: {text}\n' \
                f'email пользователя для связи: {email}'
    try:
        send = send_mail(
            'Помощь',
            mail_text,
            os.getenv("EMAIL_HOST_USER"),
            [os.getenv("TO_EMAIL"), ]
        )
        if not send:
            logger.warning("Message did'nt send")
        return send
    except Exception as e:
        logger.error(e)
        return None
