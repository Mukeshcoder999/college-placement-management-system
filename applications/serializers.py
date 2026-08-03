from rest_framework import serializers
from django.utils import timezone
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):

    student_name = serializers.CharField(
        source="student.user.username",
        read_only=True
    )
    job_title = serializers.CharField(
        source="job.title",
        read_only=True
    )
    company_name = serializers.CharField(
        source="job.company.company_name",
        read_only=True
    )
    days_left = serializers.SerializerMethodField()
    def get_days_left(self, obj):
        today = timezone.now().date()
        difference = obj.job.last_date - today

        return max(0, difference.days)




    class Meta:
        model = JobApplication
        fields = '__all__'

        read_only_fields = [
            "student"
        ]
    def validate(self, attrs):
        student = self.context["request"].user.studentprofile
        job = attrs["job"]
        today = timezone.now().date()
        if today > job.last_date:
            raise serializers.ValidationError(
            "The application deadline for this job has passed."
            )
        if student.cgpa < job.minimum_cgpa:
            raise serializers.ValidationError(
            "Your CGPA does not meet the minimum requirement for this job."
            )

        if not student.resume:
            raise serializers.ValidationError(
               "Please upload your resume before applying for a job."
            )

        if JobApplication.objects.filter(
            student=student,
            job=job
        ).exists():

            raise serializers.ValidationError(
                "You have already applied for this job."
            )
        return attrs
class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = ["status"]