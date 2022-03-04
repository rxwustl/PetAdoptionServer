from rest_framework import response, status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from posts.parsers import MultipartPostParser
from .models import Favorites, Pet, PetPost

from .serializers import FavoriteListSerializer, PetPostSerializer, PetSerializer, QueryPostSerializer


class MyPetAPIView(ListCreateAPIView):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(petowner=self.request.user)
    
    def get_queryset(self):
        return Pet.objects.filter(petowner=self.request.user)


class MyPostsAPIView(ListCreateAPIView):
    serializer_class = PetPostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        pet = Pet.objects.get(petid=int(self.request.data['petid']))
        return serializer.save(petid=pet)

    def get_queryset(self):
        return PetPost.objects.get_queryset()

class PostsAPIView(ListCreateAPIView):
    serializer_class = PetPostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return PetPost.objects.get_queryset()

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QueryPostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'postid'

    def get_queryset(self):
        return PetPost.objects.all()
    
    def perform_destroy(self, instance):
        instance.delete()
        

class FavoritesAPIView(ListAPIView):

    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'userid'

    def get_queryset(self):
        return Favorites.objects.all()
    
class AddFavoritesAPIView(CreateAPIView):

    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        postid = self.request.data.get('postid')
        post = PetPost.objects.get(postid=postid)
        return serializer.save(userid=self.request.user, postid=post)

class RemoveFavoritesAPIView(DestroyAPIView):

    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "postid"

    def perform_destroy(self, instance):
        print(instance)
    
    def get_queryset(self):
        return Favorites.objects.filter(userid=self.request.user)
        
        