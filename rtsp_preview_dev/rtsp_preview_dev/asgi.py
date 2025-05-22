"""
ASGI config for rtsp_preview_dev project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtsp_preview_dev.settings')

# application = get_asgi_application()

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import stream.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rtsp_preview_dev.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(stream.routing.websocket_urlpatterns),
})

