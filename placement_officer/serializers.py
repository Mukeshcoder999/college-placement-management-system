from rest_framework import serializers
from .models import PlacementOfficerProfile


class PlacementOfficerSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlacementOfficerProfile
        fields = '__all__'
        read_only_fields = ["user"]