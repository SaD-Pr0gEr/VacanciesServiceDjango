import os
from django.core.mail import send_mail
from dotenv import load_dotenv

load_dotenv()


def hello_user(user_email):
    try:
        send = send_mail(
            "Hello",
            'HELLO!',
            os.getenv('EMAIL_HOST_USER'),
            [user_email, ]
        )
        return send if send else None
    except Exception as e:
        print(e)
        return None
    

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
        return send if send else None
    except Exception as e:
        print(e)
        return None
