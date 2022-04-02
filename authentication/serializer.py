from rest_framework import serializers
from .models import User, UserProfilePhoto


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, write_only=True)
    displayname = serializers.CharField(max_length=128, required=False)

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('password', 'email', 'full_name', 'displayname', 'longitude', 'latitude')


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'token', 'userid', 'full_name')
        read_only_fields = ['token', 'userid', 'full_name']

class ProfilePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfilePhoto
        fields = ('userid', 'profilePhoto')

class QueryUserSerializer(serializers.ModelSerializer):

    userid = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ('userid', 'password', 'email', 'full_name', 'displayname', 'longitude', 'latitude')
        # read_only_fields = ['password', 'email', 'full_name', 'displayname', 'addressLine', 'zipcode', 'state', 'city']