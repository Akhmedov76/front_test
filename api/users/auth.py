from rest_framework.response import Response

def custom_response(data=None, message="ok", is_ok=True):
    return Response({
        "data": data,
        "isOk": is_ok,
        "message": message
    })