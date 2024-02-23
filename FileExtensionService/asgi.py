"""
ASGI config for FileExtensionService project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from file_extension.routing import websocket_urlpatterns

# Set the Django settings module for the ASGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FileExtensionService.settings')

# Get the Django ASGI application
django_asgi_app = get_asgi_application()

# Define the ASGI application routing configuration
application = ProtocolTypeRouter({
    # HTTP protocol handling
    "http": django_asgi_app,
    # WebSocket protocol handling
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
})
