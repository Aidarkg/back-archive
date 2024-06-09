from pathlib import Path
from decouple import config as env
from django.conf import settings

BASE_DIR = settings.BASE_DIR
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
