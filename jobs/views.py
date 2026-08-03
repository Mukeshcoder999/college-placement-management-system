from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer
from .filters import JobFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from accounts.permissions import IsCompany, IsJobOwner
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .pagination import JobPagination
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

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [IsAuthenticated]
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
    pagination_class = JobPagination
    
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
        IsJobOwner
    ]

#delete data

class JobDeleteAPIView(generics.DestroyAPIView):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [
        IsAuthenticated,
        IsCompany,
        IsJobOwner
    ]