from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = [
    path('', views.get_all_users),
    path('register', views.register)
]

urlpatterns = format_suffix_patterns(urlpatterns)