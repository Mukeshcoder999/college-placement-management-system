from django.urls import path
from . import views
from .views import (
    UserListAPIView, 
    UserDetailAPIView, 
    UserCreateAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    RegisterAPIView,
    LoginAPIView,
)

urlpatterns = [

    path("login/",views.login_view, name = "login"),
    path("logout/",views.logout_view, name = "logout"),
    path("student-register/",views.student_register, name = "student-register"),
    path("company-register/", views.company_register, name="company-register"),
    path("officer-register/",views.officer_register, name="officer-register"),
    path("register/",views.register, name = "register"),


    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteAPIView.as_view(), name = 'user-delete'),

    path('register/', RegisterAPIView.as_view(), name='register'),

    path('login/', LoginAPIView.as_view(), name='login'),
]
