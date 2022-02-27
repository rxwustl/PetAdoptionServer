from rest_framework import response, status
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate

from .serializer import LoginSerializer, RegisterSerializer

class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        pass

    pass


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            serializer=self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return response.Response({'message': 'Wrong username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        pass


# Create your views here.
