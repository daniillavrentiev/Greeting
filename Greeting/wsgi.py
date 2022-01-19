"""
WSGI config for Greeting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# application = WhiteNoise(application, root=settings.STATIC_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Greeting.settings')
application = get_wsgi_application()