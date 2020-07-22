"""
Django settings for twahifoundation project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e)8)$sg0m@mn5&d5t=!seug_8m&az%lc49t9%+6eeq857e8+bt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'django_extensions',
    'debug_toolbar',

    'account.apps.AccountConfig',
    'contact.apps.ContactConfig',
    'page.apps.PageConfig',
    'portal.apps.PortalConfig',
    'project.apps.ProjectConfig',
    'stock.apps.StockConfig',
    'transaction.apps.TransactionConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'twahifoundation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'twahifoundation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'twahifoundation',
        'USER': 'admin_tf',
        'PASSWORD': 'tfugbe2020',
        'HOST': 'localhost',
        'PORT': ''
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Media

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Django Extensions - Grap models
# Command for the entire project :
#   python manage.py graph_models -a -g -o graph_models/tf_visualization.png
# Command for twahifoundation model :
#   python manage.py graph_models -a -X LogEntry,ContentType,Session,AbstractBaseSession -o graph_models/sub_tf_visualization.png
# Command for twahifoundation model whitout edge model:
#   python manage.py graph_models -a --hide-edge-labels -X LogEntry,ContentType,Session,AbstractBaseSession -o graph_models/no_edge_sub_tf_visualization.png

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}


# Custom User Model

AUTH_USER_MODEL = 'account.user'

# Autjetication

LOGIN_URL = 'account:login'

LOGIN_REDIRECT_URL = 'portal:portal-home'

LOGOUT_REDIRECT_URL = 'page:home'

# Crispy Forms configuration

CRISPY_TEMPLATES_PACK = 'bootstrap4'

# Internal IPS for django-debig-toolbar

INTERNAL_IPS = [
    '127.0.0.1',
]
