from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework import generics
from .models import StudentProfile
from .serializers import StudentProfileSerializer

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

#retrive studentdata it gives only one profile at once

class StudentDetailAPIView(generics.RetrieveAPIView):

    queryset = StudentProfile.objects.all()

    serializer_class = StudentProfileSerializer

#create a students record

class StudentCreateAPIView(generics.CreateAPIView):

    queryset = StudentProfile.objects.all()

    serializer_class = StudentProfileSerializer

#update the database student record
class StudentUpdateAPIView(generics.UpdateAPIView):

    queryset = StudentProfile.objects.all()

    serializer_class = StudentProfileSerializer

#Delete a record

class StudentDeleteAPIView(generics.DestroyAPIView):

    queryset = StudentProfile.objects.all()

    serializer_class = StudentProfileSerializer