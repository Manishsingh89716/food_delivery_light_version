import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import booking_app.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "food_delivery_app.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            booking_app.routing.websocket_urlpatterns
        )
    ),
})
