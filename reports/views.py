from django.shortcuts import render
from jobs.models import Job
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count, Q
from accounts.permissions import IsStudent, IsCompany, IsPlacementOfficer
from students.models import StudentProfile
from companies.models import CompanyProfile
from applications.models import JobApplication
from notifications.models import Notification
# Create your views here.

class StudentDashboardAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request):

        student = request.user.studentprofile
        application_stats = JobApplication.objects.filter(
        student=student
                ).aggregate(
                    total_applications=Count("id"),
                    applied=Count("id", filter=Q(status="Applied")),
                    shortlisted=Count("id", filter=Q(status="Shortlisted")),
                    selected=Count("id", filter=Q(status="Selected")),
                    rejected=Count("id", filter=Q(status="Rejected")),
                )
        

        unread_notifications = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()

        data = {
            "total_applications": application_stats["total_applications"],
            "applied": application_stats["applied"],
            "shortlisted": application_stats["shortlisted"],
            "selected": application_stats["selected"],
            "rejected": application_stats["rejected"],
            "unread_notifications": unread_notifications,
        }

        return Response(data)

#comapny dashboard api view

class CompanyDashboardAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsCompany,
    ]

    def get(self, request):

        company = request.user.companyprofile

        job_stats = Job.objects.filter(
            company=company
        ).aggregate(

            jobs_posted=Count("id"),

            active_jobs=Count(
                "id",
                filter=Q(is_active=True)
            ),

            inactive_jobs=Count(
                "id",
                filter=Q(is_active=False)
            ),
        )

        application_stats = JobApplication.objects.filter(
            job__company=company
        ).aggregate(

            applications_received=Count("id"),

            shortlisted_students=Count(
                "id",
                filter=Q(status="Shortlisted")
            ),

            selected_students=Count(
                "id",
                filter=Q(status="Selected")
            ),
        )

        unread_notifications = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()

        data = {
            "jobs_posted": job_stats["jobs_posted"],
            "active_jobs": job_stats["active_jobs"],
            "inactive_jobs": job_stats["inactive_jobs"],
            "applications_received": application_stats["applications_received"],
            "shortlisted_students": application_stats["shortlisted_students"],
            "selected_students": application_stats["selected_students"],
            "unread_notifications": unread_notifications,
        }

        return Response(data)

#placement_officer dashboard 

class PlacementDashboardAPIView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsPlacementOfficer,
    ]

    def get(self, request):

        total_students = StudentProfile.objects.count()

        total_companies = CompanyProfile.objects.count()

        job_stats = Job.objects.aggregate(
            total_jobs=Count("id"),
            active_jobs=Count("id", filter=Q(is_active=True)),
            inactive_jobs=Count("id", filter=Q(is_active=False)),
        )

        application_stats = JobApplication.objects.aggregate(
            total_applications=Count("id"),
            selected_students=Count(
                "id",
                filter=Q(status="Selected")
            ),
        )

        unread_notifications = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()

        if total_students > 0:
            placement_percentage = round(
                (application_stats["selected_students"] / total_students) * 100,
                2,
            )
        else:
            placement_percentage = 0

        data = {
            "total_students": total_students,
            "total_companies": total_companies,
            "total_jobs": job_stats["total_jobs"],
            "active_jobs": job_stats["active_jobs"],
            "inactive_jobs": job_stats["inactive_jobs"],
            "total_applications": application_stats["total_applications"],
            "selected_students": application_stats["selected_students"],
            "placement_percentage": placement_percentage,
            "unread_notifications": unread_notifications,
        }

        return Response(data)