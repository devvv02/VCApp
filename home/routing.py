# yourappname/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            [
                path('ws/signal/', consumers.SignalConsumer.as_asgi()),
            ]
        )
    ),
})
