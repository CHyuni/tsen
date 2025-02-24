from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/channel/$', consumers.ChannelConsumer.as_asgi()),
]

urlpatterns = websocket_urlpatterns