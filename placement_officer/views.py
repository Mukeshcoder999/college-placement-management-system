from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PlacementOfficerProfile
from .serializers import PlacementOfficerSerializer

from students.models import StudentProfile
from companies.models import CompanyProfile
from jobs.models import Job
from applications.models import JobApplication


#placementofficer profile
@login_required
def complete_officer_profile(request):

    if request.method == "POST":

        PlacementOfficerProfile.objects.update_or_create(
        user=request.user,
        defaults={
        "employee_id": request.POST.get("employee_id"),
        "phone": request.POST.get("phone"),
        "designation": request.POST.get("designation"),
        "office_address": request.POST.get("office_address"),
        }
    )

        return redirect("officer-dashboard")

    return render(
        request,
        "placement_officer/complete_profile.html"
    )

# Create your views here.
class PlacementOfficerListAPIView(generics.ListAPIView):

    queryset = PlacementOfficerProfile.objects.all()
    serializer_class = PlacementOfficerSerializer
    permission_classes = [IsAuthenticated]

#retrieve data

class PlacementOfficerDetailAPIView(generics.RetrieveAPIView):

    serializer_class = PlacementOfficerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            PlacementOfficerProfile,
            user=self.request.user
        )

#create data

class PlacementOfficerCreateAPIView(generics.CreateAPIView):

    serializer_class = PlacementOfficerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

#update data

class PlacementOfficerUpdateAPIView(generics.UpdateAPIView):

    serializer_class = PlacementOfficerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            PlacementOfficerProfile,
            user=self.request.user
        )

#delete data

class PlacementOfficerDeleteAPIView(generics.DestroyAPIView):

    serializer_class = PlacementOfficerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            PlacementOfficerProfile,
            user=self.request.user
        )

#officer profile exists API VIEW

class PlacementOfficerProfileExistsAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        exists = PlacementOfficerProfile.objects.filter(
            user=request.user
        ).exists()

        return Response({
            "exists": exists
        })
# placementOfficerdashboard APIVIEW

class PlacementOfficerDashboardAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = StudentProfile.objects.count()

        companies = CompanyProfile.objects.count()

        jobs = Job.objects.count()

        applications = JobApplication.objects.count()

        selected_students = JobApplication.objects.filter(
            status="Selected"
        ).count()

        if students > 0:

            placement_percentage = round(

                (selected_students / students) * 100,

                2

            )

        else:

            placement_percentage = 0

        recent_jobs = Job.objects.select_related(
            "company"
        ).order_by("-created_at")[:5]

        recent_applications = JobApplication.objects.select_related(
            "student__user",
            "job"
        ).order_by("-application_date")[:5]

        return Response({

            "students": students,

            "companies": companies,

            "jobs": jobs,

            "applications": applications,

            "selected_students": selected_students,

            "placement_percentage": placement_percentage,

            "recent_jobs": [

                {

                    "title": job.job_title,

                    "company": job.company.company_name,

                }

                for job in recent_jobs

            ],

            "recent_applications": [

                {

                    "student": application.student.user.username,

                    "job": application.job.job_title,

                    "status": application.status,

                }

                for application in recent_applications

            ]

        })