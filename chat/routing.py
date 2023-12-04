from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<int:room_pk>/", consumers.RolePlayingRoomConsumer.as_asgi()),
    #as_view 대신 as_asgi
] # ws://localhost:8000/ws/chat/1/ 이런식으로 됨