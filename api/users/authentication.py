from rest_framework import authentication
from rest_framework import exceptions

from api.users.models import UserAuth


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('Key')
        signature = request.headers.get('Sign')

        if not api_key or not signature:
            return None

        try:
            user = UserAuth.objects.get(key=api_key)

            print(f"Received Key: {api_key}")
            print(f"Received Sign: {signature}")
            print(f"Stored secret: {user.secret}")

            if signature != user.secret:
                raise exceptions.AuthenticationFailed('Invalid signature')

            return (user, None)

        except UserAuth.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid API key')
