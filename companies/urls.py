from django.urls import path
from . import views
from .views import (
    CompanyListAPIView,
    CompanyDetailAPIView,
    CompanyCreateAPIView,
    CompanyUpdateAPIView,
    CompanyDeleteAPIView,
)


urlpatterns = [
    path("complete-profile/",views.complete_company_profile, name = "company-profile"),


    path('', CompanyListAPIView.as_view(), name='company-list'),
    path('<int:pk>/', CompanyDetailAPIView.as_view(), name='company-detail'),
    path('create/', CompanyCreateAPIView.as_view(), name='company-create'),
    path('<int:pk>/update/', CompanyUpdateAPIView.as_view(), name='company-update'),
    path('<int:pk>/delete/', CompanyDeleteAPIView.as_view(), name='company-delete'),

    
]
