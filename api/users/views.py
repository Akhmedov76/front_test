from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserAuth
from .serializers import UserAuthSerializer


class SignupView(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "isOk": True,
                "message": "ok"
            }, status=status.HTTP_200_OK)
        return Response({
            "isOk": False,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
