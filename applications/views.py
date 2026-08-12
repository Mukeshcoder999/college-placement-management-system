from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from students.models import StudentProfile
from students.serializers import StudentProfileSerializer
from accounts.permissions import (
    IsStudent, IsCompany, 
    IsPlacementOfficer, IsApplicationAccessible,
    CanUpdateApplication,
)
from placement_project.pagination import CustomPagination
from django.db import transaction
from notifications.models import Notification
from .models import JobApplication
from .serializers import JobApplicationSerializer, ApplicationStatusUpdateSerializer

# Create your views here.

class JobApplicationListAPIView(generics.ListAPIView):

    queryset = JobApplication.objects.all()

    serializer_class = JobApplicationSerializer

    permission_classes = [
        IsAuthenticated,
        
    ]
    pagination_class = CustomPagination
    

    def get_queryset(self):
        user = self.request.user

        queryset = JobApplication.objects.select_related(
            "student",
            "student__user",
            "job",
            "job__company"
        )

        print(queryset.query)

        if user.role == "student":
            return queryset.filter(
                student=user.studentprofile
            )

        elif user.role == "company":
            return queryset.filter(
                job__company=user.companyprofile
            )

        elif user.role == "placement_officer":
            return queryset


        return JobApplication.objects.none()

#Retive data

class JobApplicationDetailAPIView(generics.RetrieveAPIView):

    queryset = JobApplication.objects.all()

    serializer_class = JobApplicationSerializer

    permission_classes = [IsAuthenticated, IsApplicationAccessible]

#create data

class JobApplicationCreateAPIView(generics.CreateAPIView):

    queryset = JobApplication.objects.all()

    serializer_class = JobApplicationSerializer

    permission_classes = [IsAuthenticated, IsStudent]

    def perform_create(self, serializer):

        serializer.save(
            student=self.request.user.studentprofile
        )

#update data

class JobApplicationUpdateAPIView(generics.UpdateAPIView):

    queryset = JobApplication.objects.all()

    serializer_class = ApplicationStatusUpdateSerializer

    permission_classes = [
        IsAuthenticated,
        CanUpdateApplication,
        IsApplicationAccessible
    ]

    @transaction.atomic
    def perform_update(self, serializer):

        application = serializer.save()

        if application.status == "Shortlisted":

            Notification.objects.create(

                recipient=application.student.user,

                title="Application Shortlisted",

                message=f"Congratulations! You have been shortlisted for {application.job.job_title}."

            )

        elif application.status == "Selected":

            Notification.objects.create(

                recipient=application.student.user,

                title="Application Selected",

                message=f"Congratulations! You have been selected for {application.job.job_title}."

            )

        elif application.status == "Rejected":

            Notification.objects.create(

                recipient=application.student.user,

                title="Application Rejected",

                message=f"Your application for {application.job.job_title} was not selected."

            )

#delete data

class JobApplicationDeleteAPIView(generics.DestroyAPIView):

    queryset = JobApplication.objects.all()

    serializer_class = JobApplicationSerializer

    permission_classes = [
        IsAuthenticated,
        IsApplicationAccessible
    ]

#company view
class CompanyApplicationListAPIView(generics.ListAPIView):

    serializer_class = JobApplicationSerializer

    permission_classes = [
        IsAuthenticated,
        IsCompany
    ]
    pagination_class = CustomPagination


    def get_queryset(self):
        return JobApplication.objects.filter(
            job__company=self.request.user.companyprofile
        )

#placementofficerview

class AllApplicationsAPIView(generics.ListAPIView):

    queryset = JobApplication.objects.all()

    serializer_class = JobApplicationSerializer

    permission_classes = [
        IsAuthenticated,
        IsPlacementOfficer
    ]
    pagination_class = CustomPagination

class ApplicantDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):

        student = get_object_or_404(
            StudentProfile,
            id=student_id
        )

        serializer = StudentProfileSerializer(
            student,
            context={"request": request}
        )

        return Response(serializer.data)