from django.shortcuts import render, redirect 
from .services import register_user
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
# Create your views here.


#login.html
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == "student":
                return redirect("student-profile")

            elif user.role == "company":
                return redirect("company-profile")

            elif user.role == "officer":
                return redirect("officer-profile")

            else:

                messages.error(
                    request,
                    "Invalid Username or Password"
                )

    return render(
        request,
        "accounts/login.html"
    )
#logoutview
def logout_view(request):

    logout(request)

    messages.success(request, "Logged out successfully.")

    return redirect("home")


#student_register.html
def student_register(request):

    if request.method == "POST":

        user = register_user(request, "student")

        if user:
            login(request, user)          # <-- Add this line
            return redirect("student-profile")

    return render(request, "accounts/student_register.html")

#company register
def company_register(request):

    if request.method == "POST":

        user = register_user(request, "company")

        if user:
            login(request, user)
            return redirect("company-profile")

    return render(request, "accounts/company_register.html")


#placement_officer register.html
def officer_register(request):

    if request.method == "POST":

        user = register_user(request, "officer")

        if user:
            login(request, user)
            return redirect("officer-profile")

    return render(request, "accounts/officer_register.html")
#register.html

def register(request):
    return render(request, "accounts/register.html")



class UserListAPIView(generics.ListAPIView):

    queryset = CustomUser.objects.all()

    serializer_class = UserSerializer

#returns one user at once 
class UserDetailAPIView(generics.RetrieveAPIView):

    queryset = CustomUser.objects.all()

    serializer_class = UserSerializer

#this is will create a new user in the database
class UserCreateAPIView(generics.CreateAPIView):

    queryset = CustomUser.objects.all()

    serializer_class = UserSerializer
#update the user information
class UserUpdateAPIView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()

    serializer_class = UserSerializer
#delete a record 
class UserDeleteAPIView(generics.DestroyAPIView):

    queryset = CustomUser.objects.all()

    serializer_class = UserSerializer

#create Register ApiView

class RegisterAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    serializer_class = RegisterSerializer

#create a LoginAPI View

@extend_schema(
    request=LoginSerializer,
    responses={200: None},
    tags=["Accounts"],
    summary="User Login"
)
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

       

        refresh = RefreshToken.for_user(user)

        access = refresh.access_token

        return Response(
            {
                "access": str(access),
                "refresh": str(refresh),

                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                }
            },
            status=status.HTTP_200_OK
        )


