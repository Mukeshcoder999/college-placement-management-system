from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import PlacementOfficerProfile
from .serializers import PlacementOfficerSerializer


#placementofficer profile
@login_required
def complete_officer_profile(request):

    if request.method == "POST":

        PlacementOfficerProfile.objects.update_or_create(
        user=request.user,
        defaults={
        "employee_id": request.POST.get("employee_id"),
        "phone": request.POST.get("phone"),
        "designation": request.POST.get("designation"),
        "office_address": request.POST.get("office_address"),
        }
    )

        return redirect("officer-dashboard")

    return render(
        request,
        "placement_officer/complete_profile.html"
    )




# Create your views here.
class PlacementOfficerListAPIView(generics.ListAPIView):

    queryset = PlacementOfficerProfile.objects.all()

    serializer_class = PlacementOfficerSerializer

#retrieve data

class PlacementOfficerDetailAPIView(generics.RetrieveAPIView):

    queryset = PlacementOfficerProfile.objects.all()

    serializer_class = PlacementOfficerSerializer

#create data

class PlacementOfficerCreateAPIView(generics.CreateAPIView):

    queryset = PlacementOfficerProfile.objects.all()

    serializer_class = PlacementOfficerSerializer

#update data

class PlacementOfficerUpdateAPIView(generics.UpdateAPIView):

    queryset = PlacementOfficerProfile.objects.all()

    serializer_class = PlacementOfficerSerializer

#delete data

class PlacementOfficerDeleteAPIView(generics.DestroyAPIView):

    queryset = PlacementOfficerProfile.objects.all()

    serializer_class = PlacementOfficerSerializer