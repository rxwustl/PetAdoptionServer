from rest_framework import response, status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Pet, PetPost

from .serializers import PetPostSerializer, PetSerializer, QueryPostSerializer


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

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return PetPost.objects.get_queryset()

class PostsAPIView(ListCreateAPIView):
    serializer_class = PetPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PetPost.objects.get_queryset()

class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = QueryPostSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'postid'

    def get_queryset(self):
        return PetPost.objects.all()

    

