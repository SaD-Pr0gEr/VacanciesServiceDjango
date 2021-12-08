import os
from celery import Celery
from celery.schedules import crontab

try:
    from vacansies_service.settings import dev
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vacansies_service.settings.dev")
except ImportError:
    from vacansies_service.settings import prod
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vacansies_service.settings.prod")


app = Celery('vacansies_service')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'parse-vacancy-every-day': {
        'task': "main_app.tasks.run_parser_1",
        "schedule": crontab(hour="*/23")
    }
}
