from rest_framework import serializers
from .models import CustomUser


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

    def to_representation(self, ins):
        return {
            "id": ins.id,
            "username": ins.username,
            "first_name": ins.first_name,
            "last_name": ins.last_name,
            "email": ins.email
        }
