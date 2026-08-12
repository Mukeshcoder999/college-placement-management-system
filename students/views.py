from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentProfile
from .serializers import StudentProfileSerializer
from jobs.models import Job
from applications.models import JobApplication
from notifications.models import Notification
from accounts.permissions import IsPlacementOfficer
from placement_project.pagination import CustomPagination


from rest_framework.permissions import IsAuthenticated

#studentprofile
@login_required
def complete_student_profile(request):

    if request.method == "POST":

        StudentProfile.objects.update_or_create(
    user=request.user,
    defaults={
        "phone": request.POST.get("phone"),
        "gender": request.POST.get("gender"),
        "date_of_birth": request.POST.get("date_of_birth"),
        "college_name": request.POST.get("college_name"),
        "course": request.POST.get("course"),
        "branch": request.POST.get("branch"),
        "passing_year": request.POST.get("passing_year"),
        "cgpa": request.POST.get("cgpa"),
        "address": request.POST.get("address"),
        "skills": request.POST.get("skills"),
        "resume": request.FILES.get("resume"),
        "profile_picture": request.FILES.get("profile_picture"),
    }
)

        return redirect("student-dashboard")

    return render(
        request,
        "students/complete_profile.html"
    )

# Create your views here.


class StudentListAPIView(generics.ListAPIView):

    queryset = StudentProfile.objects.all()

    serializer_class = StudentProfileSerializer

    permission_classes = [IsAuthenticated]

    pagination_class = CustomPagination

#retrive studentdata it gives only one profile at once

class StudentDetailAPIView(generics.RetrieveAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            StudentProfile,
            user=self.request.user
        )

#create a students record

class StudentCreateAPIView(generics.CreateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
#student profile ExistsAPIVIEW
class StudentProfileExistsAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        exists = StudentProfile.objects.filter(
            user=request.user
        ).exists()

        return Response({
            "exists": exists
        })

#update the database student record
class StudentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            StudentProfile,
            user=self.request.user
        )

#Delete a record

class StudentDeleteAPIView(generics.DestroyAPIView):

    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(
            StudentProfile,
            user=self.request.user
        )


#student profile Apiview
class StudentProfileAPIView(generics.RetrieveAPIView):

    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.studentprofile

#studentProfile update ApI

class StudentProfileUpdateAPIView(generics.UpdateAPIView):

    serializer_class = StudentProfileSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.studentprofile

#student dashboard API View 

class StudentDashboardAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        student = request.user.studentprofile

        print("Logged User:", request.user.username)
        print("Student Profile ID:", student.id)

        available_jobs = Job.objects.filter(is_active=True).count()
        print("Available Jobs:", available_jobs)

        applied_jobs = JobApplication.objects.filter(
            student=student
        ).count()
        print("Applied Jobs:", applied_jobs)

        notifications = Notification.objects.filter(
            recipient=request.user
        ).count()

        recent_jobs = Job.objects.filter(
            is_active=True
        ).order_by("-created_at")[:5]

        recent_notifications = Notification.objects.filter(
            recipient=request.user
        ).order_by("-created_at")[:5]

        return Response({
            "available_jobs": available_jobs,
            "applied_jobs": applied_jobs,
            "notifications": notifications,
            "recent_jobs": [job.job_title for job in recent_jobs],
            "recent_notifications": [
                notification.message
                for notification in recent_notifications
            ],
        })
#placementOfficer studentApIView

class AllStudentsAPIView(generics.ListAPIView):

    serializer_class = StudentProfileSerializer

    permission_classes = [
        IsAuthenticated,
        IsPlacementOfficer
    ]
    pagination_class = CustomPagination
    queryset = StudentProfile.objects.select_related(
        "user"
    ).all()