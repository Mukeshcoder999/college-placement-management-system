from django.contrib import admin
from .models import JobApplication

# Register your models here.
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'student',
        'job',
        'status',
        'application_date',
    )

    search_fields = (
        'student__user__username',
        'job__job_title',
    )

    list_filter = (
        'status',
    )

    ordering = ('-application_date',)