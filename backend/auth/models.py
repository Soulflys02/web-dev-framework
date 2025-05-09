from django.db import models
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed

# Create your models here.
class CookieJWTAuthentication(JWTAuthentication):
    """
    Custom JWT Authentication class that uses cookies for token storage.
    """
    def authenticate(self, request):
        access_token = request.COOKIES.get('access_token')
        if not access_token:
            return None
        try:
            validated_token = self.get_validated_token(access_token)
            return self.get_user(validated_token), validated_token
        except AuthenticationFailed:
            return None
