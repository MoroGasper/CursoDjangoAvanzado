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
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '543522529087814'
SOCIAL_AUTH_FACEBOOK_SECRET = '6fd2112f339247355b14c4647e8d5f46'

SOCIAL_AUTH_TWITTER_KEY = '89NnhGfzBa8MwOCkztqzgWkBn'
SOCIAL_AUTH_TWITTER_SECRET = 'ndyJcw9vGvqMotv9JWUSMu75aci5Nk89GI2WDTYUDbe2X8P36p'