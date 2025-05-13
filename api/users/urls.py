from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.users.views import UserAuthViewSet

router = DefaultRouter()

router.register(r'signup', UserAuthViewSet, basename='signup')

urlpatterns = [
    path('', include(router.urls))
]
