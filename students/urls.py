from django.urls import path 
from . import views
from .views import (
    StudentListAPIView, 
    StudentDetailAPIView,
    StudentCreateAPIView,
    StudentUpdateAPIView,
    StudentDeleteAPIView,
)


urlpatterns = [
    path("complete-profile/", views.complete_student_profile, name = "student-profile"),


    path('', StudentListAPIView.as_view(), name='student-list'),
    path('<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('create/', StudentCreateAPIView.as_view(), name='student-create'),
    path('<int:pk>/update/', StudentUpdateAPIView.as_view(), name='student-update'),
    path('<int:pk>/delete/', StudentDeleteAPIView.as_view(), name='student-delete'),

]
