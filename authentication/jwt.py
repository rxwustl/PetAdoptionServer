import jwt
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from authentication.models import User
from rest_framework import exceptions
from django.conf import settings


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        header = get_authorization_header(request)
        print(request)
        print(header)
        content = header.decode('utf-8')
        if len(content.split(' ')) == 2:
            token = content.split(' ')[1]
            pass
        else:
            raise exceptions.AuthenticationFailed("Invalid authentication header")
        
        try:
            decoded_info = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            email = decoded_info['email']
            user = User.objects.get(email=email)
            return (user, token)
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Invalid Token")
            pass
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("The Token Has Expired")
            pass
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("The user does not exist")
            pass
        
