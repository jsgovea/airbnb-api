from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.GET.get('HTTP_AUTHORIZATION')
        if token is None:
            return None
        xjwt, jwt_token = token.split(' ')
        
