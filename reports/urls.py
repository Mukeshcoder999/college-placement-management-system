from django.urls import path
from .views import StudentDashboardAPIView, CompanyDashboardAPIView, PlacementDashboardAPIView

urlpatterns = [
    path(
        "student-dashboard/",
        StudentDashboardAPIView.as_view(),
        name="student-dashboard", 
    ),
    path(
        "company-dashboard/",
        CompanyDashboardAPIView.as_view(),
        name="company-dashboard",
    ),
    path(
        "placement-dashboard/",
        PlacementDashboardAPIView.as_view(),
        name="placement-dashboard",
    ),
]
