from django.urls import path
from . import views
from .views import (
    CompanyListAPIView,
    CompanyDetailAPIView,
    CompanyCreateAPIView,
    CompanyUpdateAPIView,
    CompanyDeleteAPIView,
    CompanyProfileExistsAPIView,
    CompanyProfileAPIView,
    CompanyProfileUpdateAPIView,
    CompanyDashboardAPIView,
    AllCompaniesAPIView,
    CompanyDetailsAPIView,
)


urlpatterns = [
    path("complete-profile/",views.complete_company_profile, name = "company-profile"),

    path("api/profile/",CompanyProfileExistsAPIView.as_view(),name="company-profile-exists"),
    path("profile/", CompanyProfileAPIView.as_view(), name="company-profile"),

    path("profile/update/", CompanyProfileUpdateAPIView.as_view(),name="company-profile-update"),
    path("dashboard/", CompanyDashboardAPIView.as_view(), name="company-dashboard"),
    path("all/", AllCompaniesAPIView.as_view(), name="all-companies"),

    path("details/<int:pk>/", CompanyDetailsAPIView.as_view(),name="company-details"),

    path('api/', CompanyListAPIView.as_view(), name='company-list'),
    path('api/<int:pk>/', CompanyDetailAPIView.as_view(), name='company-detail'),
    path('api/create/', CompanyCreateAPIView.as_view(), name='company-create'),
    path('api/<int:pk>/update/', CompanyUpdateAPIView.as_view(), name='company-update'),
    path('api/<int:pk>/delete/', CompanyDeleteAPIView.as_view(), name='company-delete'),

    
]
