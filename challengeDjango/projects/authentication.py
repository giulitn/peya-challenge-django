from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import requests

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')
        if not authorization_header or 'bearer' not in authorization_header.lower():
            return None

        token = authorization_header.split(' ')[1]
        response = requests.get('http://backend:3000/auth/me', headers={'Authorization': f'Bearer {token}'})
        
        if response.status_code == 200:
            user_data = response.json()
            User = get_user_model()
            user, _ = User.objects.get_or_create(username=user_data['email'], defaults={'email': user_data['email']})
            return (user, None)  
        else:
            raise exceptions.AuthenticationFailed('Token is invalid or expired')
