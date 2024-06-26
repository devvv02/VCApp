"""
ASGI config for vcsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from home.routing import application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vcsite.settings')

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": application,
})
application = get_asgi_application()
