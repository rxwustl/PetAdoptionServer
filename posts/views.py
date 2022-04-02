import math
from rest_framework import response, status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import SearchFilter
from django.db.utils import IntegrityError
from posts.filters import PostFilter
from django.db.models import F, Value, FloatField, ExpressionWrapper

from posts.parsers import MultipartPostParser
from .models import Favorites, Pet, PetPost
from .serializers import FavoriteListSerializer, PetPostSerializer, PetSerializer, QueryPostSerializer
from posts import serializers
from django_filters.rest_framework import DjangoFilterBackend


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
        # print(self.request.data['image'])
        pet = Pet.objects.get(petid=int(self.request.data['petid']))
        return serializer.save(petid=pet)

    def get_queryset(self):
        try:
            return PetPost.objects.filter(petid__in=Pet.objects.filter(petowner=self.request.user))
        except Pet.DoesNotExist:
            return PetPost.objects.none()


class PostsAPIView(ListCreateAPIView):
    serializer_class = PetPostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    filterset_class = PostFilter
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['petid__petname', 'desc', 'petid__breed']

    def get_queryset(self):
        return PetPost.objects.get_queryset().annotate(dist=ExpressionWrapper(
                    (F('petid__petowner__latitude') - self.request.user.latitude) ** 2 +
                    (F('petid__petowner__longitude') - self.request.user.longitude) ** 2,
                    output_field=FloatField()
                )
            ).order_by('dist')


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

    def get_queryset(self):
        return Favorites.objects.filter(userid=self.request.user)
    

class AddFavoritesAPIView(CreateAPIView):

    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return self.perform_create(serializer)
        else:
            return response.Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    
    def perform_create(self, serializer):
        postid = self.request.data.get('postid')
        post = PetPost.objects.get(postid=postid)
        try:
            serializer.save(userid=self.request.user, postid=post)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError as ie:
            return response.Response({'detail': str(ie)}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFavoritesAPIView(DestroyAPIView):

    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'postid'

    def perform_destroy(self, instance):
        return instance.delete()

    # def delete(self, request, *args, **kwargs):
    #     self.get_queryset().filter(postid=PetPost.objects.get(postid=int(self.kwargs.get('postid')))).delete()
    #     return response.Response(status.HTTP_204_NO_CONTENT)
    
    def get_queryset(self):
        return Favorites.objects.filter(userid=self.request.user)
        
        