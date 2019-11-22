from . import views
from django.urls import path, include

app_name = 'user'
urlpatterns = [
    path('login/', views.user_login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('profile_edit/', views.profile_edit, name = 'profile_edit'),
    path('upload_avatar/', views.upload_avatar, name = 'upload_avatar'),
    path('logout/', views.user_logout, name = 'logout'),
]