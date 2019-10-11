from django.urls import path
from . import views

app_name = 'room'
urlpatterns = [
    path('self_chat_room', views.self_chat_room, name='self_chat_room'),
    path('', views.chat, name='chat-url')
]