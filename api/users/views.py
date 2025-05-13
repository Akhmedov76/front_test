from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.users.auth import custom_response
from .models import UserAuth
from .serializers import UserAuthSerializer


class UserAuthViewSet(viewsets.GenericViewSet):
    queryset = UserAuth.objects.all()
    serializer_class = UserAuthSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=UserAuthSerializer)
    @action(detail=False, methods=['POST'], url_path="signup", permission_classes=[AllowAny])
    def user_signup(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return custom_response(
                data=serializer.data,
                message="User successfully created",
                is_ok=True
            )
        except Exception as e:
            return custom_response(
                data=None,
                message=str(e),
                is_ok=False
            )

    @swagger_auto_schema(
        operation_description="Get user information",
        responses={200: UserAuthSerializer},
        manual_parameters=[
            openapi.Parameter(
                'Key',
                openapi.IN_HEADER,
                description="API Key",
                type=openapi.TYPE_STRING,
                required=True
            ),
            openapi.Parameter(
                'Sign',
                openapi.IN_HEADER,
                description="Request signature",
                type=openapi.TYPE_STRING,
                required=True
            ),
        ]
    )
    @action(detail=False, methods=['GET'], url_path='myself')
    def myself(self, request):
        try:
            if request.user.is_superuser:
                queryset = self.get_queryset()
                serializer = self.get_serializer(queryset, many=True)
            else:
                serializer = self.get_serializer(request.user)
            return custom_response(
                data=serializer.data,
                message="Success",
                is_ok=True
            )
        except Exception as e:
            return custom_response(
                data=None,
                message=str(e),
                is_ok=False
            )
