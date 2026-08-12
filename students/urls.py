from django.urls import path 
from . import views
from .views import (
    StudentListAPIView, 
    StudentDetailAPIView,
    StudentCreateAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
    StudentProfileExistsAPIView,
    StudentProfileAPIView,
    StudentProfileUpdateAPIView,
    StudentDashboardAPIView,
    AllStudentsAPIView,

)


urlpatterns = [
    path("complete-profile/", views.complete_student_profile, name = "student-profile"),

    path("api/profile/", StudentProfileExistsAPIView.as_view(), name="student-profile-exists"),
    path("profile/", StudentProfileAPIView.as_view(), name="student-profile"),
    path("profile/update/", StudentProfileUpdateAPIView.as_view(),name="student-profile-update"),
    path("dashboard/", StudentDashboardAPIView.as_view(), name="student-dashboard"),
    path("all/", AllStudentsAPIView.as_view(), name="all-students"),

    path('api/', StudentListAPIView.as_view(), name='student-list'),
    path('api/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('api/create/', StudentCreateAPIView.as_view(), name='student-create'),
    path('api/<int:pk>/update/', StudentUpdateAPIView.as_view(), name='student-update'),
    path('api/<int:pk>/delete/', StudentDeleteAPIView.as_view(), name='student-delete'),
    
]
