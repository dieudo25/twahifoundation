from .base import *


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False


ALLOWED_HOSTS = ['IP-ADDRESS', 'www.yourwebsite.com']


# Paypal

PAYPAL_RECEIVER_EMAIL = os.getenv('PAYPAL_ACCOUNT')
PAYPAL_TEST = True
