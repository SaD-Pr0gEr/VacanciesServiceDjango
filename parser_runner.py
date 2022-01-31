# import random
# import time
# from main_app.parser import *
# import os
# import sys
#
#
# runner_path = os.path.dirname(os.path.abspath('manage.py'))
# sys.path.append(runner_path)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'vacancies_service.settings.dev'
#
# import django
# django.setup()
#
# from main_app.models import ProgramLanguage
#
#
# if __name__ == "__main__":
#     languages = ProgramLanguage.objects.all()
#     user_agents = [
#         "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36",
#         "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36",
#         "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)",
#         "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056)"
#     ]
#     HEADERS = {
#         "User-Agent": random.choice(user_agents),
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
#     }
#     while True:
#         runner_work_ua(languages, HEADERS)
#         get_links = geek_job_links(languages, HEADERS)
#         get_jobs_info = parser_geek_job(get_links, HEADERS)
#         print("all ok")
#         time.sleep(85000)
