#!/usr/bin/env python

import os
import sys

import yaml

if __name__ == "__main__":
    config = os.path.join(os.getcwd(), 'env.yml')
    if os.path.isfile(config):
        config = yaml.load(open(config, 'r').read())
        for key, value in config['ENV_VARS'].items():
            os.environ.setdefault(key, value)
    else:
        raise Exception('env.yml not found, please create one')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mentors.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
