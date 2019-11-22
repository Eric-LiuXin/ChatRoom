from django.urls import path
from . import views

app_name = 'room'
urlpatterns = [
    path('self_chat_room/', views.self_chat_room, name='self_chat_room'),
    path('join_room/', views.join_room, name='join_room'),
    path('user_card/<int:user_id>/', views.user_card, name='user_card'),
    path('', views.chat, name='chat-url')
]