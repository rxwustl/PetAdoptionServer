from dataclasses import fields
from rest_framework import serializers
from .models import User, UserPreference, UserProfilePhoto


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
        fields = ('email', 'password', 'token', 'userid', 'full_name', 'profilePhoto')
        read_only_fields = ['token', 'userid', 'full_name', 'profilePhoto']

class ProfilePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('userid', 'profilePhoto')

class QueryUserSerializer(serializers.ModelSerializer):

    userid = serializers.IntegerField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('userid', 'email', 'full_name', 'displayname', 'longitude', 'latitude', 'profilePhoto', 'password')
        # read_only_fields = ['password', 'email', 'full_name', 'displayname', 'addressLine', 'zipcode', 'state', 'city']

class UserPrefSerializer(serializers.ModelSerializer):

    # userid = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserPreference
        fields = ('pettype', 'age', 'breed', 'gender', 'hairlength', 'weight')
        lookup_field = 'userid'
    
class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('full_name')

class UpdateLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('longitude', 'latitude')

class ChangePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password')