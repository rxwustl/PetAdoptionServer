from authentication import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name='register'),
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('profile_photo', views.UserPhoto.as_view(), name='profile'),
    path('user', views.UserAPIView.as_view(), name='user'),
    path('update_profile', views.UpdateProfileAPIView.as_view(), name='update_profile'),
    path('update_location', views.UpdateLocationAPIView.as_view(), name='update_loc'),
    path('preference', views.UserPreferenceAPIView.as_view(), name="preference")
]