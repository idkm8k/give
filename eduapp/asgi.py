import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import ADA.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduapp.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ADA.routing.websocket_urlpatterns
        )
    ),
})
