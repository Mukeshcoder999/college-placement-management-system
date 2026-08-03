from django.contrib import admin
from .models import Job
# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'job_title',
        'company',
        'location',
        'salary',
        'vacancies',
        'job_type',
        'last_date',
        'is_active',
    )

    search_fields = (
        'job_title',
        'company__company_name',
    )

    list_filter = (
        'job_type',
        'is_active',
        'location',
    )

    ordering = ('-created_at',)