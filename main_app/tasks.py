from main_app.email_senders import hello_user, help_sender
from vacansies_service.celery import app
# import random
# from main_app.models import ProgramLanguage
# from main_app.parser import runner_work_ua, geek_job_links, parser_geek_job


# languages = ProgramLanguage.objects.all()
# user_agents = [
#     "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36",
#     "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36",
#     "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)",
#     "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056)"
# ]
# HEADERS = {
#     "User-Agent": random.choice(user_agents),
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
# }


@app.task
def hello_sender(user_email):
    send = hello_user(user_email)
    return send


@app.task
def help_send(name, email, text):
    send = help_sender(name, email, text)
    return send

# @app.task
# def run_parser_1():
#     res = runner_work_ua(languages, HEADERS)
#     return res if res else None
#
#
# @app.task
# def run_parser_2():
#     get_links = geek_job_links(languages, HEADERS)
#     res = parser_geek_job(get_links, HEADERS)
#     return res if res else None
