import uuid
from django.db import models

from authentication.models import User
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    filename = filename.split('.')
    filename = filename[0] + '_' + uuid.uuid4().hex + '.' + filename[1]
    return 'posts/{filename}'.format(filename=filename)


class Pet(models.Model):
    CAT = 'CAT'
    DOG = 'DOG'
    PET_TYPE_CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog')
    ]
    MALE = 'M'
    FEMALE = 'F'
    GENDER_TYPE_CHOICES = [
        (MALE, 'M'),
        (FEMALE, 'F')
    ]
    SHORT = 'S'
    MEDIUM = 'M'
    LONG = 'L'
    HAIR_LENGTH_CHOICES = [
        (SHORT, 'S'),
        (MEDIUM, 'M'),
        (LONG, 'L')
    ]
    petid = models.AutoField(primary_key=True)
    gender = models.CharField(choices=GENDER_TYPE_CHOICES, max_length=2, blank=False, default='M')
    petname = models.CharField(max_length=64, blank=False)
    pettype = models.CharField(choices=PET_TYPE_CHOICES, max_length=4, blank=False)
    breed = models.CharField(max_length=128)
    age_year = models.IntegerField(blank=False)
    age_month = models.IntegerField(blank=False)
    birthday = models.DateField()
    neutered = models.BooleanField()
    weight = models.FloatField(default=10)
    hairlength = models.CharField(choices=HAIR_LENGTH_CHOICES, default='M', max_length=4)
    petowner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="petowner")


class PetPost(models.Model):
    postdate = models.DateTimeField(auto_now_add=True)
    petid = models.ForeignKey(to=Pet, on_delete=models.CASCADE, related_name='pet')
    desc = models.TextField()
    postid = models.AutoField(primary_key=True)
    closed = models.BooleanField(default=False)
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='posts/default.jpg')
    pass


class Favorites(models.Model):
    userid = models.ForeignKey(to=User, on_delete=models.CASCADE)
    postid = models.ForeignKey(to=PetPost, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        unique_together = ('userid', 'postid',)
    
# Create your models here.
