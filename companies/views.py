from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsPlacementOfficer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CompanyProfile
from .serializers import CompanyProfileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from placement_project.pagination import CustomPagination
from jobs.models import Job
from applications.models import JobApplication


#companyprofile
@login_required
def complete_company_profile(request):

    if request.method == "POST":

        CompanyProfile.objects.update_or_create(
    user=request.user,
    defaults={
        "company_name": request.POST.get("company_name"),
        "company_email": request.POST.get("company_email"),
        "phone": request.POST.get("phone"),
        "website": request.POST.get("website"),
        "address": request.POST.get("address"),
        "description": request.POST.get("description"),
        "established_year": request.POST.get("established_year"),
        "logo": request.FILES.get("logo"),
    }
)

        return redirect("company-dashboard")

    return render(
        request,
        "companies/complete_profile.html"
    )

# Create your views here.
class CompanyListAPIView(generics.ListAPIView):

    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

#retrive data

class CompanyDetailAPIView(generics.RetrieveAPIView):

    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            CompanyProfile,
            user=self.request.user
        )

#create data

class CompanyCreateAPIView(generics.CreateAPIView):

    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#update data

class CompanyUpdateAPIView(generics.UpdateAPIView):

    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            CompanyProfile,
            user=self.request.user
        )

#delete data

class CompanyDeleteAPIView(generics.DestroyAPIView):

    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            CompanyProfile,
            user=self.request.user
        )

#company profile Exists API Checking

class CompanyProfileExistsAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        exists = CompanyProfile.objects.filter(
            user=request.user
        ).exists()

        return Response({
            "exists": exists
        })
#company profile api view
class CompanyProfileAPIView(generics.RetrieveAPIView):

    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):

        return get_object_or_404(
            CompanyProfile,
            user=self.request.user
        )


class CompanyProfileUpdateAPIView(generics.UpdateAPIView):

    serializer_class = CompanyProfileSerializer
    permission_classes = [IsAuthenticated]

    parser_classes = [MultiPartParser, FormParser]

    def get_object(self):

        return get_object_or_404(
            CompanyProfile,
            user=self.request.user
        )

#company dashboardapiview 

class CompanyDashboardAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        company = request.user.companyprofile

        active_jobs = Job.objects.filter(
            company=company,
            is_active=True
        ).count()

        applications = JobApplication.objects.filter(
            job__company=company
        ).count()

        selected = JobApplication.objects.filter(
            job__company=company,
            status="Selected"
        ).count()

        recent_jobs = Job.objects.filter(
            company=company
        ).order_by("-created_at")[:5]

        recent_applications = JobApplication.objects.filter(
            job__company=company
        ).select_related(
            "student__user",
            "job"
        ).order_by("-application_date")[:5]

        return Response({

            "active_jobs": active_jobs,

            "applications": applications,

            "selected": selected,

            "recent_jobs":[
                job.job_title
                for job in recent_jobs
            ],

            "recent_applications":[
                {
                    "student": application.student.user.username,
                    "job": application.job.job_title,
                }
                for application in recent_applications
            ]

        })

class AllCompaniesAPIView(generics.ListAPIView):

    queryset = CompanyProfile.objects.all().select_related("user")

    serializer_class = CompanyProfileSerializer

    permission_classes = [
        IsAuthenticated,
        IsPlacementOfficer
    ]
    pagination_class = CustomPagination

class CompanyDetailsAPIView(generics.RetrieveAPIView):

    queryset = CompanyProfile.objects.select_related("user")

    serializer_class = CompanyProfileSerializer

    permission_classes = [
        IsAuthenticated,
        IsPlacementOfficer
    ]