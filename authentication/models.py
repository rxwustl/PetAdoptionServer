from email.policy import default
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
import jwt
from django.conf import settings
from datetime import datetime, timedelta
# Create your models here.

class PetUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    pass



def upload_to(instance, filename):
    filename = filename.split('.')
    filename = filename[0] + '_' + uuid.uuid4().hex + '.' + filename[1]
    return 'profile/{filename}'.format(filename=filename)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=False, unique=True)
    userid = models.AutoField(primary_key=True)
    full_name = models.CharField(_('full_name'), max_length=150, blank=False, default="")
    displayname = models.CharField(_('displayname'), max_length=150, blank=True, default="")
    latitude = models.FloatField(_('latitude'), blank=False, default=0)
    longitude = models.FloatField(_('longitude'), blank=False, default=0)
    profilePhoto = models.ImageField(_('profilePhoto'), blank=True, default=None, upload_to=upload_to)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_superuser = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def token(self):
        token = jwt.encode(
            {'email': self.email, 'exp': datetime.utcnow() + timedelta(days=30)},
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return token

    objects = PetUserManager()  

class UserProfilePhoto(models.Model):
    userid = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="user")
    profilePhoto = models.ImageField(upload_to=upload_to, default="default.jpeg")
    pass


class UserPreference(models.Model):
    userid = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='pref_user', unique=True)
    pettype = models.CharField(max_length=4, default='N')
    age = models.CharField(default="N", max_length=4)
    gender = models.CharField(default='N', max_length=4)
    hairlength = models.CharField(default='N', max_length=4)
    weight = models.CharField(default="N", max_length=4)
    

