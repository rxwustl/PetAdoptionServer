from authentication import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('profile_photo', views.UserPhoto.as_view(), name='profile'),
    path('user', views.UserAPIView.as_view(), name='user')
]