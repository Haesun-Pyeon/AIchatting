import os
from channels.routing import ProtocolTypeRouter,  URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django_asgi_app = get_asgi_application()

import chat.routing # 장고 앱 초기화 다음에 와야함! 위에X

application = ProtocolTypeRouter({
    "http": django_asgi_app, #http는 장고가 처리
    "websocket": AuthMiddlewareStack(
            URLRouter(chat.routing.websocket_urlpatterns),
            #websocket이 오면 채널스가 직접 처리?
        ),
})