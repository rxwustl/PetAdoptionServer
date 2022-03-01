from unicodedata import name
from authentication import views
from django.urls import path
from .views import MyPetAPIView, MyPostsAPIView, PostDetailAPIView, PostsAPIView

urlpatterns = [
    path('mypet', MyPetAPIView.as_view(), name='mypet'),
    path('myposts', MyPostsAPIView.as_view(), name='myposts'),
    path('posts', PostsAPIView.as_view(), name='posts'),
    path('<int:postid>', PostDetailAPIView.as_view(), name='pdetail')
]