from django.urls import re_path
from . import consumers

# WebSocket route must match frontend (chat.js) path => /ws/chat/<room_id>/
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]