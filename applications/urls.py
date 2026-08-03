from django.urls import path
from .views import (
    JobApplicationListAPIView,
    JobApplicationDetailAPIView,
    JobApplicationCreateAPIView,
    JobApplicationUpdateAPIView,
    JobApplicationDeleteAPIView,
    CompanyApplicationListAPIView,
    AllApplicationsAPIView,
)

urlpatterns = [
    path('', JobApplicationListAPIView.as_view(), name='application-list'),
    path('<int:pk>/', JobApplicationDetailAPIView.as_view(), name='application-detail'),
    path('create/', JobApplicationCreateAPIView.as_view(), name='application-create'),
    path('<int:pk>/update/', JobApplicationUpdateAPIView.as_view(), name='application-update'),
    path('<int:pk>/delete/', JobApplicationDeleteAPIView.as_view(), name='application-delete'),
    path('company/', CompanyApplicationListAPIView.as_view(),
         name='company-application-list'),

    path('all/', AllApplicationsAPIView.as_view(),
         name='all-application-list'),
]
