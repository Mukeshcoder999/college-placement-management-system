from django.contrib import admin
from .models import CompanyProfile

# Register your models here.

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'company_name',
        'company_email',
        'phone',
        'website',
        'created_at',
    )

    search_fields = (
        'company_name',
        'company_email',
    )

    ordering = ('-created_at',)