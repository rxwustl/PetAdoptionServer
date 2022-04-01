from django.forms import ImageField
from rest_framework import serializers

from authentication.serializer import RegisterSerializer
from .models import Favorites, Pet, PetPost

class PetSerializer(serializers.ModelSerializer):

    # petowner = RegisterSerializer()

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
            "petid",
        ]
        read_only_fields = ['petid']
        depth = 2
    pass

class PetPostSerializer(serializers.ModelSerializer):

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



