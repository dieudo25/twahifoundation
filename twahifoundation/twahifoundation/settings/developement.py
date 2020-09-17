from .base import *

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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Media

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Paypal

PAYPAL_RECEIVER_EMAIL = os.getenv('PAYPAL_ACCOUNT')
PAYPAL_TEST = True
