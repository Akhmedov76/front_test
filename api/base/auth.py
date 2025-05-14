from rest_framework.response import Response


def custom_response(data=None, message="ok", is_ok=True):
    return Response({
        "data": data,
        "isOk": is_ok,
        "message": message
    })


from api.users.models import UserAuth


def get_user_by_key(key: str):
    try:
        return UserAuth.objects.get(key=key)
    except UserAuth.DoesNotExist:
        return None


def is_valid_signature(key: str, sign: str, isbn: str) -> bool:
    try:
        user = UserAuth.objects.get(key=key)
        return sign == user.secret
    except UserAuth.DoesNotExist:
        return False
