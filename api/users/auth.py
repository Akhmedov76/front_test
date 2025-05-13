import hashlib
from .models import User


def verify_signature(request):
    key = request.headers.get('Key')
    sign = request.headers.get('Sign')

    if not key or not sign:
        return False

    try:
        user = User.objects.get(key=key)
    except User.DoesNotExist:
        return False

    raw_string = key + user.secret
    expected_sign = hashlib.md5(raw_string.encode()).hexdigest()

    return expected_sign == sign
