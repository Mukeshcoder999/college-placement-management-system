from rest_framework import serializers
from .models import StudentProfile
import os


class StudentProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    resume = serializers.SerializerMethodField()

    def get_resume(self, obj):

        if not obj.resume:
            return None

        # Check if the file actually exists
        if not os.path.exists(obj.resume.path):
            return None

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.resume.url)

        return obj.resume.url

    class Meta:
        model = StudentProfile
        fields = "__all__"
        read_only_fields = ["user"]