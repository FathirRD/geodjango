from django.urls import path

from . import views

app_name    = 'status'

urlpatterns = [
    path('status/',                    views.index,                name='index'),
    path('status/<str:room_name>/',    views.room,                 name='room'),
]