from . import views
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('sign_up/', views.user_sign_up, name = 'user_sign_up'),
]