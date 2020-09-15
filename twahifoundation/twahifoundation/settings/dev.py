from .base import *


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True


ALLOWED_HOSTS = ['*']


INSTALLED_APPS += [
    'debug_toolbar',
]


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# Internal IPS for django-debug-toolbar

INTERNAL_IPS = [
    '127.0.0.1',
]


# Paypal

PAYPAL_TEST = False
