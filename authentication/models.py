from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
import jwt
from django.conf import settings
from datetime import datetime, timedelta
# Create your models here.

class PetUserManager(UserManager):
    def _create_user(self, username, email, password, full_name, displayname, addressLine, zipcode, state, city):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        username = self.model.normalize_username(username)
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, addressLine=addressLine, zipcode=zipcode, state=state, full_name=full_name, displayname=displayname, city=city)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, full_name, displayname, addressLine, zipcode, state, city, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, full_name, displayname, addressLine, zipcode, state, city)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    pass


class User(AbstractUser):
    
    userid = models.AutoField(primary_key=True)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    full_name = models.CharField(_('full_name'), max_length=150, blank=False, default="")
    displayname = models.CharField(_('displayname'), max_length=150, blank=True, default="")
    email = models.EmailField(_('email address'), blank=False, default="")
    addressLine = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=6)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=64, default='')

    @property
    def token(self):
        token = jwt.encode(
            {'username': self.username, 'email': self.email, 'exp': datetime.utcnow() + timedelta(days=30)},
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return token

    objects = PetUserManager()
        


