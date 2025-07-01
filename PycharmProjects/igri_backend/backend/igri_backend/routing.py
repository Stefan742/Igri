from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application


application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # ОБАВЕЗНО за HTTP да функционира Django API и admin
    "websocket": AuthMiddlewareStack(
        URLRouter(
            backend.matches.routing.websocket_urlpatterns
        )
    ),
})
