from django.urls import path
from . import views

app_name = 'room'
urlpatterns = [
    path('echo_once/', views.echo_once, name='echo_once'),
    path('echo/', views.echo, name='echo'),
    path('modify_message/', views.modify_message, name='modify_message'),
    path('index2/', views.index2, name='index2'),
    path('', views.index, name='index'),
]