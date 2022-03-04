from unicodedata import name
from authentication import views
from django.urls import path
from .views import AddFavoritesAPIView, FavoritesAPIView, MyPetAPIView, MyPostsAPIView, PostDetailAPIView, PostsAPIView, RemoveFavoritesAPIView

urlpatterns = [
    path('mypet', MyPetAPIView.as_view(), name='mypet'),
    path('myposts', MyPostsAPIView.as_view(), name='myposts'),
    path('posts', PostsAPIView.as_view(), name='posts'),
    path('<int:postid>', PostDetailAPIView.as_view(), name='pdetail'),
    path('favorites/', FavoritesAPIView.as_view(), name="favlist"),
    path('favorites/add', AddFavoritesAPIView.as_view(), name="addfav"),
    path('favorites/remove/<int:postid>', RemoveFavoritesAPIView.as_view(), name="removefav"),
    
]