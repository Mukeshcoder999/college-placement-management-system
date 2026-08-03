from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import CompanyProfile
from .serializers import CompanyProfileSerializer


#companyprofile
@login_required
def complete_company_profile(request):

    if request.method == "POST":

        CompanyProfile.objects.update_or_create(
    user=request.user,
    defaults={
        "company_name": request.POST.get("company_name"),
        "company_email": request.POST.get("company_email"),
        "phone": request.POST.get("phone"),
        "website": request.POST.get("website"),
        "address": request.POST.get("address"),
        "description": request.POST.get("description"),
        "established_year": request.POST.get("established_year"),
        "logo": request.FILES.get("logo"),
    }
)

        return redirect("company-dashboard")

    return render(
        request,
        "companies/complete_profile.html"
    )

# Create your views here.
class CompanyListAPIView(generics.ListAPIView):

    queryset = CompanyProfile.objects.all()

    serializer_class = CompanyProfileSerializer

#retrive data

class CompanyDetailAPIView(generics.RetrieveAPIView):

    queryset = CompanyProfile.objects.all()

    serializer_class = CompanyProfileSerializer

#create data

class CompanyCreateAPIView(generics.CreateAPIView):

    queryset = CompanyProfile.objects.all()

    serializer_class = CompanyProfileSerializer

#update data

class CompanyUpdateAPIView(generics.UpdateAPIView):

    queryset = CompanyProfile.objects.all()

    serializer_class = CompanyProfileSerializer

#delete data

class CompanyDeleteAPIView(generics.DestroyAPIView):

    queryset = CompanyProfile.objects.all()

    serializer_class = CompanyProfileSerializer