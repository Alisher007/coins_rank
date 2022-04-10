from django.urls import path

from .consumers import CoinsConsumer

ws_urlspatterns = [
    path('ws/coins/', CoinsConsumer.as_asgi())
]