from django.contrib import messages
from .models import CustomUser


def register_user(request, role):

    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")

    if password != confirm_password:
        messages.error(request, "Passwords do not match.")
        return None

    if CustomUser.objects.filter(username=username).exists():
        messages.error(request, "Username already exists.")
        return None

    if CustomUser.objects.filter(email=email).exists():
        messages.error(request, "Email already exists.")
        return None

    # Create the user and store it
    user = CustomUser.objects.create_user(
        username=username,
        email=email,
        password=password,
        role=role
    )

    messages.success(request, "Registration Successful.")

    # Return the created user object
    return user