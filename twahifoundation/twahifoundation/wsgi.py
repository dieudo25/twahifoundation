"""
WSGI config for twahifoundation project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from importlib.util import find_spec

production_module_exists = find_spec(
    "twahifoundation.settings.production") is not None

if production_module_exists:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'twahifoundation.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'twahifoundation.settings.developement')

application = get_wsgi_application()
