from .base import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-&t4=ark(ongg4_@g=5$x+l4caiag(gb98nys$&p1d%-r5c1r9i'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
