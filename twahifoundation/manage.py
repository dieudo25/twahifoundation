#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from importlib.util import find_spec


def main():

    production_module_exists = find_spec(
        "twahifoundation.settings.production") is not None

    if production_module_exists:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'twahifoundation.settings.production')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'twahifoundation.settings.developement')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
