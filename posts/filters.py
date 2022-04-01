from dataclasses import fields
import django_filters

from posts.models import PetPost


class PostFilter(django_filters.FilterSet):
    breed = django_filters.CharFilter(field_name='petid__breed')
    age = django_filters.CharFilter(field_name='petid__age_year')
    type = django_filters.CharFilter(field_name='petid__pettype')
    neutered = django_filters.BooleanFilter(field_name='petid__neutered')
    gender = django_filters.CharFilter(field_name='petid__gender')
    class Meta:
        model = PetPost
        fields = ['breed', 'age', 'type', 'neutered', 'gender']