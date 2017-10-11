import os

import yaml
from django.core.wsgi import get_wsgi_application

config = os.path.join(os.getcwd(), 'env.yml')
if os.path.isfile(config):
    config = yaml.load(open(config, 'r').read())
    for key, value in config['ENV_VARS'].items():
        os.environ.setdefault(key, value)
else:
    raise Exception('env.yml not found, please create one')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mentors.settings")

application = get_wsgi_application()
