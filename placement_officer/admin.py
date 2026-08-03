from django.contrib import admin
from .models import PlacementOfficerProfile
# Register your models here.


@admin.register(PlacementOfficerProfile)
class PlacementOfficerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'employee_id',
        'phone',
        'designation',
    )

    search_fields = (
        'user__username',
        'employee_id',
    )

    ordering = ('employee_id',)