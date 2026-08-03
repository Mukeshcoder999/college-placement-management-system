from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser

        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'role'
        ]

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'role',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):

        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {"password": "Password and Confirm Password do not match."}
            )

        return attrs

    def create(self, validated_data):

        validated_data.pop('confirm_password')

        password = validated_data.pop('password')

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError(
                {
                    "error": "Invalid username or password."
                }
            )

        attrs['user'] = user

        return attrs
