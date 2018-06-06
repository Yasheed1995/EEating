"""
WSGI config for eeating project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '..', 'site-packages'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eeating.settings")

application = get_wsgi_application()

