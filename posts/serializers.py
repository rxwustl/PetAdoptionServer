from dataclasses import fields
from django.forms import ImageField
from rest_framework import serializers
from authentication.models import User

from authentication.serializer import RegisterSerializer, QueryUserSerializer
from .models import Favorites, Pet, PetPost

class PetOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ('email', 'full_name', 'displayname', 'longitude', 'latitude', 'profilePhoto')
        read_only_fields = ('email', 'full_name', 'displayname', 'longitude', 'latitude', 'profilePhoto')
        depth = 2

class PetSerializer(serializers.ModelSerializer):

    # petowner = PetOwnerSerializer()

    class Meta:
        model = Pet
        fields = [
            "petname",
            "gender",
            "pettype",
            "breed",
            "age_year",
            "age_month",
            "birthday",
            "neutered",
            'weight',
            'hairlength',
            # 'petowner',
            "petid",
        ]
        read_only_fields = ['petid']
        depth = 2
    pass



class PetPostSerializer(serializers.ModelSerializer):

    # petid = PetSerializer()

    class Meta:
        model = PetPost
        fields = ('petid', 'desc', 'postid', 'image')
        read_only_fields = ['postid']
        depth = 2

class QueryPostSerializer(serializers.ModelSerializer):

    pet = PetSerializer(many=True, read_only=True)

    class Meta:
        model = PetPost
        fields = ('petid', 'desc', 'postid', 'pet', 'image')
        depth = 2
    
class FavoriteListSerializer(serializers.ModelSerializer):

    # userid = serializers.IntegerField(write_only=True)
    posts = PetPostSerializer(many=True, read_only=True)
    class Meta:
        model = Favorites
        fields = ('posts', 'postid',)
        lookup_field = 'userid'
        depth = 2
        write_only_fields = ['postid']



