#!/usr/local/bin/python
# coding: utf-8

import os
# from collections import OrderedDict as SortedDict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r6zfm1@g^!qz8r@v!w*kl^z&s0&oxf1g5u5md!^1tv4-!xsbem'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
EMAIL_HOST = 'mail.barbastrosemueve.es'
EMAIL_HOST_USER = 'info@barbastrosemueve.es'
EMAIL_HOST_PASSWORD = 'Barbastro2017'
EMAIL_PORT = 587
EMAIL_USE_TLS = False

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'healthylifeapp',
    'rest_framework',
    'guardian',
    'ckeditor',
    'taggit',
    'corsheaders',
    'datetimewidget'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'healthylife.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                    os.path.join(BASE_DIR, "templates"),
                    BASE_DIR + '/templates/blog/',
                    BASE_DIR + '/templates/shop/',
                    BASE_DIR + '/templates/sport/',
                    BASE_DIR + '/templates/health/',
                    BASE_DIR + '/templates/nutrition/',
                    BASE_DIR + '/templates/registration/',
                    BASE_DIR + '/templates/awards/',
                    BASE_DIR + '/templates/calendar/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'healthylife.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'healthylifedb',
        'USER': 'dbadminuser',
        'PASSWORD': 'Barbastro2017',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # BASE_DIR + '/images/',
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")

# Static files

MEDIA_URL = '/media/'

"""
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "media"),
    BASE_DIR + '/photos/',
]
"""

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

LOGIN_URL = 'custom_login'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = [
    'healthylifeapp.backend.CustomBackend',
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
    ]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        # 'toolbar': None
        'toolbar': 'Full'
    }
}

# CORS, to allow all origin to the api during development
# https://github.com/zestedesavoir/django-cors-middleware
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1',
)

CORS_ORIGIN_ALLOW_ALL = True

CORS_URLS_ALLOW_ALL_REGEX = (

)

CORS_URLS_ALLOW_ALL = True
