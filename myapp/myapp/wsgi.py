"""
WSGI config for myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# sync to -> /home/ubuntu/myapp/manage.py(os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings.production"))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings.dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings.production")

application = get_wsgi_application()
