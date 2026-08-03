from django.urls import path 
from .views import (
    JobListAPIView,
    JobDetailAPIView,
    JobCreateAPIView,
    JobUpdateAPIView,
    JobDeleteAPIView,
)

urlpatterns = [
    path('', JobListAPIView.as_view(), name='job-list'),
    path('<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),
    path('create/', JobCreateAPIView.as_view(), name='job-create'),
    path('<int:pk>/update/', JobUpdateAPIView.as_view(), name='job-update'),
    path('<int:pk>/delete/', JobDeleteAPIView.as_view(), name='job-delete'),
    
]
