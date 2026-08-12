from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer
from .filters import JobFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from accounts.permissions import IsCompany, IsJobOwner, CanDeleteJob
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .pagination import JobPagination
from rest_framework.views import APIView
from rest_framework.response import Response


import logging
# Create your views here.
logger = logging.getLogger(__name__)

@extend_schema(
    summary="List Jobs",
    description=(
        "Retrieve all available jobs. "
        "Supports filtering, searching, ordering, and pagination."
    ),
    tags=["Jobs"],
)
class JobListAPIView(generics.ListAPIView):

    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = JobPagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = JobFilter
    search_fields = [
        "job_title",
        "required_skills",
        "company__company_name",
    ]
    ordering_fields = [
        "salary",
        "minimum_cgpa",
        "last_date",
        "created_at",
    ]

    def get_queryset(self):
        user = self.request.user

        if user.role == "company":

            return Job.objects.filter(
                company=user.companyprofile
            )

        elif user.role == "placement_officer":

            return Job.objects.all()

        return Job.objects.filter(
            is_active=True
        )
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
        
    
#retrive data
class JobDetailAPIView(generics.RetrieveAPIView):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

#create data

class JobCreateAPIView(generics.CreateAPIView):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [IsAuthenticated, IsCompany]

    def perform_create(self, serializer):
        job = serializer.save(
        company=self.request.user.companyprofile
    )

        logger.info(
             f"Job '{job.job_title}' created by user '{self.request.user.username}'"
    )

#update data

class JobUpdateAPIView(generics.UpdateAPIView):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [
        IsAuthenticated,
        IsCompany,
        IsJobOwner,
    ]

#delete data

class JobDeleteAPIView(generics.DestroyAPIView):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [
        IsAuthenticated,
        CanDeleteJob
    ]


class ToggleJobStatusAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsCompany,
        IsJobOwner,
    ]

    def patch(self, request, pk):

        job = Job.objects.get(pk=pk)

        self.check_object_permissions(request, job)

        job.is_active = not job.is_active

        job.save()

        return Response({

            "message": "Job status updated successfully.",

            "is_active": job.is_active,

        })
