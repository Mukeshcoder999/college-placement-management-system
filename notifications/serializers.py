from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'

    def validate_title(self, value):

        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Title must contain at least 5 characters."
            )

        return value

    def validate_message(self, value):

        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "Message must contain at least 10 characters."
            )

        return value