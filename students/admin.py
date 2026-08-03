from django.contrib import admin
from .models import StudentProfile


# Register your models here.

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'phone',
        'college_name',
        'course',
        'branch',
        'passing_year',
        'cgpa',
        'created_at',
    )

    search_fields = (
        'user__username',
        'college_name',
        'course',
        'branch',
    )

    list_filter = (
        'passing_year',
        'course',
    )

    ordering = ('-created_at',)