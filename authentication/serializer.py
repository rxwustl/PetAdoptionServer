from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('password', 'email', 'full_name', 'displayname', 'addressLine', 'zipcode', 'state', 'city')


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('password', 'token')
        read_only_fields = ['token']