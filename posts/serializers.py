from django.forms import ImageField
from rest_framework import serializers
from .models import Favorites, Pet, PetPost

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = [
            "petname",
            "pettype",
            "breed",
            "age_year",
            "age_month",
            "birthday",
            "neutered",
            "petid"
        ]
        read_only_fields = ['petid']
        depth = 1
    pass

class PetPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetPost
        fields = ('petid', 'desc', 'postid', 'image')
        read_only_fields = ['postid']
        depth = 1

class QueryPostSerializer(serializers.ModelSerializer):

    pet = PetSerializer(many=True, read_only=True)

    class Meta:
        model = PetPost
        fields = ('petid', 'desc', 'postid', 'pet', 'image')
        depth = 1
    
class FavoriteListSerializer(serializers.ModelSerializer):

    # userid = serializers.IntegerField(write_only=True)
    posts = PetPostSerializer(many=True, read_only=True)
    class Meta:
        model = Favorites
        fields = ('posts', 'postid',)
        lookup_field = 'userid'
        depth = 2
        write_only_fields = ['postid']



