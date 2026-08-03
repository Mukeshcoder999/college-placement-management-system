from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import (
    IsStudent, IsCompany, 
    IsPlacementOfficer, IsApplicationAccessible,
    CanUpdateApplication,
)
from django.db import transaction

from .models import JobApplication
from .serializers import JobApplicationSerializer, ApplicationStatusUpdateSerializer

# Create your views here.

class JobApplicationListAPIView(generics.ListAPIView):

    queryset = JobApplication.objects.all()

    serializer_class = JobApplicationSerializer

    permission_classes = [
        IsAuthenticated,
        
    ]

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