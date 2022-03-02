"""
ASGI config for geodjango project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth      import AuthMiddlewareStack
from channels.routing   import ProtocolTypeRouter, URLRouter

from django.core.asgi   import get_asgi_application

from kgis.api           import routing as status_route

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geodjango.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            status_route.websocket_urlpatterns
        )
    ),
})