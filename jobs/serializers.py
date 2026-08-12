from rest_framework import serializers
from .models import Job
from applications.models import JobApplication


class JobSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(
        source="company.company_name",
        read_only=True
    )

    applied = serializers.SerializerMethodField()
    application_count = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"

        read_only_fields = ["company"]

    def get_applied(self, obj):

        request = self.context.get("request")

        if not request:
            return False

        user = request.user

        if not user.is_authenticated:
            return False

        if user.role != "student":
            return False

        return JobApplication.objects.filter(
            student=user.studentprofile,
            job=obj
        ).exists()
    def get_application_count(self, obj):

        return JobApplication.objects.filter(
            job=obj
        ).count()