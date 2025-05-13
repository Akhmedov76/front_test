from rest_framework import serializers

from api.users.models import UserAuth


class UserAuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAuth
        fields = ('id', 'name', 'email', 'key', 'secret', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = UserAuth.objects.create_user(
            name=validated_data.pop('name'),
            email=validated_data.pop('email'),
            password=password,
            **validated_data
        )
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
