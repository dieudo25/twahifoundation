"""
Django settings for twahifoundation project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django_archive import archivers
from dotenv import load_dotenv


load_dotenv(verbose=True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'bootstrap_datepicker_plus',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'django_archive',
    'django_extensions',
    'paypal.standard.ipn',
    'import_export',
    'notifications',

    'account.apps.AccountConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'message.apps.MessageConfig',
    'newsletter.apps.NewsletterConfig',
    'page.apps.PageConfig',
    'portal.apps.PortalConfig',
    'project.apps.ProjectConfig',
    'stock.apps.StockConfig',
    'transaction.apps.TransactionConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'HOST': os.getenv("DATABASE_HOST"),
        'PORT': os.getenv("DATABASE_PORT"),
    }
}

SITE_ID = 1


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
LANGUAGES = [
    ('en', 'English'),
    ('fr', 'French'),
]

TIME_ZONE = 'Europe/Brussels'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Static
STATIC_URL = '/static/'

# Media

MEDIA_URL = '/media/'

# SMTP configuration

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")


# Custom User Model

AUTH_USER_MODEL = 'account.user'


# Authentication

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'portal:portal-home'
LOGOUT_REDIRECT_URL = 'page:home'


# Crispy Forms configuration

CRISPY_TEMPLATES_PACK = 'bootstrap4'


# Django Extensions - Grap models
# Command for the entire project :
#   python manage.py graph_models -a -g -o graph_models/tf_visualization.png
# Command for twahifoundation model (excluding) :
#   python manage.py graph_models -a -X LogEntry,ContentType,Session,AbstractBaseSession -o graph_models/sub_tf_visualization.png
# Command for twahifoundation model (including) :
#   python manage.py graph_models -a -I User,Group,Permission,Company,Person,Event,Project,Stock,Product,ProductStockTransfert,Category,Task,Transaction,ProductTransactionLine,Message,Post,Tags -o graph_models/sub_tf_visualization2.png
# Command for twahifoundation model whitout edge model:
#   python manage.py graph_models -a --hide-edge-labels -I User,Group,Permission,Company,Person,Event,Project,Stock,Product,ProductStockTransfert,Category,Task,Transaction,ProductTransactionLine,Message,Post,Tags  -o graph_models/no_edge_sub_tf_visualization.png

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}


# Mail Chimp

MAILCHIMP_API_KEY = os.getenv('TF_API_KEY')
MAILCHIMP_DATA_CENTER = os.getenv('TF_DATA_CENTER')
MAILCHIMP_EMAIL_LIST_ID = os.getenv('TF_EMAIL_LIST_ID')

# Date Picker

BOOTSTRAP4 = {
    'include_jquery': False,
}

# Django archive

ARCHIVE_FORMAT = archivers.ZIP

# CKEditor

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'office2013',
        'toolbar': 'toolbarGroups',  # put selected toolbar config here
        'toolbarGroups': [
            {
                'name': 'document', 'groups': ['mode', 'document', 'doctools']
            },

            {
                'name': 'clipboard', 'groups': ['undo']
            },

            {
                'name': 'styles', 'groups': ['styles'],
            },

            {
                'name': 'basicstyles', 'groups': ['basicstyles', 'cleanup']
            },

            {
                'name': 'colors', 'groups': ['colors']
            },

            {
                'name': 'editing', 'groups': [

                    'find', 'selection', 'spellchecker', 'editing']
            },

            {
                'name': 'paragraph', 'groups': [

                    'indent', 'blocks', 'align', 'list', 'bidi', 'paragraph']
            },

            {
                'name': 'links', 'groups': ['links']
            },

            {
                'name': 'insert', 'groups': ['insert']
            },

            {
                'name': 'tools', 'groups': ['tools']
            },

            {
                'name': 'others', 'groups': ['others', 'youtube']
            },


        ],
        'extraPlugins': ','.join(
            ['youtube', 'autolink', ]
        ),
        'tabSpaces': 4,
    },
    'full': {
        'toolbar': 'Basic',
    },
}
