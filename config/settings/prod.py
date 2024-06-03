from .base import *

DEBUG = True

INSTALLED_APPS += ['debug_toolbar', ]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = '/usr/src/app/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/usr/src/app/media/'


CSRF_TRUSTED_ORIGINS = ["http://localhost", "http://localhost:82"]