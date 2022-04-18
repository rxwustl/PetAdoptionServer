from rest_framework import response, status, permissions
from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend

from authentication.models import User, UserProfilePhoto
from posts import serializers

from .serializer import LoginSerializer, ProfilePhotoSerializer, RegisterSerializer, QueryUserSerializer


class UserAPIView(RetrieveAPIView, UpdateAPIView):

    permission_classes = [IsAuthenticated]

    def retrieve(self, request):
        serializer = QueryUserSerializer(instance=request.user)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
        # return User.objects.get(userid=self.request.data['userid'])

class UserPhoto(CreateAPIView, RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProfilePhotoSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['userid']

    def retrieve(self, request):
        instance = User.objects.get(userid=self.request.user.userid)
        serializer = ProfilePhotoSerializer(data={
            "email": instance.email,
            "profilePhoto": instance.profilePhoto
        })
        if serializer.is_valid():
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        # print(request.data)
        # serializer = self.serializer_class(data={
        #     'userid': request.user.userid,
        #     'profilePhoto': request.data['photo'] 
        # })
        # if serializer.is_valid():
        #     serializer.save(userid=request.user, profilePhoto=request.data['photo'])
        #     return response.Response(serializer.data, status.HTTP_201_CREATED)
        # else:
        #     return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # pass
        photo = request.data['photo']
        serializer = self.serializer_class(request.user, data={
            'userid': request.user.userid,
            'profilePhoto': photo
        }, partial=True)
        if serializer.is_valid():
            # serializer.update(instance=request.user, validated_data=serializer.validated_data)
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # User.objects.filter(userid=request.user.userid).update(profilePhoto=photo)



class RegisterAPIView(GenericAPIView):

    authentication_classes = []
    serializer_class = RegisterSerializer

    def post(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        if user:
            serializer=self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response({'message': 'Wrong username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        pass


# Create your views here.
