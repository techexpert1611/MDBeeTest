from django.urls import re_path
from . import consumers

# Define WebSocket URL patterns for routing WebSocket connections to consumers
websocket_urlpatterns = [
    # Define a WebSocket URL pattern that matches the path 'ws/file_extension/'
    re_path(r"ws/file_extension/$", consumers.FileExtensionConsumer.as_asgi()),
]
