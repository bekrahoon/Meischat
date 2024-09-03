from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<group_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/online-tracker/$', consumers.OnlineTrackerConsumer.as_asgi()),

]
