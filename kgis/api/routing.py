from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/api/perangkat/$',                      consumers.PerangkatConsumer.as_asgi()),
    re_path(r'ws/api/monitor/$',                        consumers.DataMonitorConsumer.as_asgi()),
    re_path(r'ws/api/monitor/(?P<perangkat>\w+)/$',     consumers.PerangkatMonitorConsumer.as_asgi()),
]