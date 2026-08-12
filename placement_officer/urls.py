from django.urls import path 
from . import views
from .views import (
    PlacementOfficerListAPIView,
    PlacementOfficerDetailAPIView,
    PlacementOfficerCreateAPIView,
    PlacementOfficerUpdateAPIView,
    PlacementOfficerDeleteAPIView,
    PlacementOfficerProfileExistsAPIView,
    PlacementOfficerDashboardAPIView,
)

urlpatterns = [
    path("complete-profile/", views.complete_officer_profile,name = "officer-profile"),


    path("api/profile/", PlacementOfficerProfileExistsAPIView.as_view(), name="officer-profile-exists"),
    path("dashboard/", PlacementOfficerDashboardAPIView.as_view(), name="officer-dashboard"),

    path('api/', PlacementOfficerListAPIView.as_view(), name='officer-list'),
    path('api/<int:pk>/', PlacementOfficerDetailAPIView.as_view(), name='officer-detail'),
    path('api/create/', PlacementOfficerCreateAPIView.as_view(), name='officer-create'),
    path('api/<int:pk>/update/', PlacementOfficerUpdateAPIView.as_view(), name='officer-update'),
    path('api/<int:pk>/delete/', PlacementOfficerDeleteAPIView.as_view(), name='officer-delete'),
    
]

