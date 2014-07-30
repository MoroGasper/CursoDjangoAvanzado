# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'postgres',
        'PASSWORD': 'Inicio0313',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'