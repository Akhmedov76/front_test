from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import UserAuth
from .serializers import UserAuthSerializer


class UserAuthViewSet(viewsets.ModelViewSet):
    queryset = UserAuth.objects.all()
    serializer_class = UserAuthSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(query_serializer=UserAuthSerializer)
    @action(detail=False, methods=['POST'], url_path="signup", permission_classes=[AllowAny])
    def user_signup(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
