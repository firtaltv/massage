from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    PasswordField,
)

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "profile_photo",
        )
        read_only_fields = (
            "username",
            "email",
        )


class LoginSerializer(TokenObtainPairSerializer):

    password = PasswordField(write_only=True)

    class Meta:
        fields = ("password",)
