from django.urls import path 
from . import views
from .views import (
    PlacementOfficerListAPIView,
    PlacementOfficerDetailAPIView,
    PlacementOfficerCreateAPIView,
    PlacementOfficerUpdateAPIView,
    PlacementOfficerDeleteAPIView,
)

urlpatterns = [
    path("complete-profile/", views.complete_officer_profile,name = "officer-profile"),



    path('', PlacementOfficerListAPIView.as_view(), name='officer-list'),
    path('<int:pk>/', PlacementOfficerDetailAPIView.as_view(), name='officer-detail'),
    path('create/', PlacementOfficerCreateAPIView.as_view(), name='officer-create'),
    path('<int:pk>/update/', PlacementOfficerUpdateAPIView.as_view(), name='officer-update'),
    path('<int:pk>/delete/', PlacementOfficerDeleteAPIView.as_view(), name='officer-delete'),
    
]

