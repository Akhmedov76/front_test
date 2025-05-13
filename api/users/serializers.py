from rest_framework import serializers
from .models import UserAuth

class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = ['id', 'name', 'email', 'key', 'secret']
