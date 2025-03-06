"""
WSGI config for sticky_notes_project project.

This file is used for deployment.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "sticky_notes_project.settings"
)

application = get_wsgi_application()
