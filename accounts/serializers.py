from rest_framework import serializers
from .models import CustomUser
import re
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

        password = attrs["password"]

        confirm_password = attrs["confirm_password"]

        if len(password) < 6:

            raise serializers.ValidationError({

                "password": "Password must be at least 6 characters long."

            })

        if not re.search(r"[A-Z]", password):

            raise serializers.ValidationError({

                "password": "Password must contain at least one uppercase letter."

            })

        if not re.search(r"[a-z]", password):

            raise serializers.ValidationError({

                "password": "Password must contain at least one lowercase letter."

            })

        if not re.search(r"\d", password):

            raise serializers.ValidationError({

                "password": "Password must contain at least one number."

            })

        if password != confirm_password:

            raise serializers.ValidationError({

                "confirm_password": "Password and Confirm Password do not match."

            })

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
        username = attrs.get("username")

        password = attrs.get("password")

        user = User.objects.filter(
            username=username
        ).first()

        if not user:

            raise serializers.ValidationError({

                "username": "Invalid Username"

            })

        authenticated_user = authenticate(

            username=username,

            password=password

        )

        if not authenticated_user:

            raise serializers.ValidationError({

                "password": "Incorrect password."

            })

        attrs["user"] = authenticated_user

        return attrs
