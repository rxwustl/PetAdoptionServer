from rest_framework import serializers
from .models import Pet, PetPost

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
        depth=1
    pass

class PetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetPost
        fields = ('petid', 'desc', 'postid')
        read_only_fields = ['postid']

class QueryPostSerializer(serializers.ModelSerializer):

    pet = PetSerializer(many=True, read_only=True)

    class Meta:
        model = PetPost
        fields = ('petid', 'desc', 'postid', 'pet')
        depth=1
    
