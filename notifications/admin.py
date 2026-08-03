from django.contrib import admin
from .models import Notification
# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        "recipient",
        'title',
        'is_read',
        'created_at',
    )

    search_fields = (
        "recipient__username",
        'title',
    )

    list_filter = (
        'is_read',
    )

    ordering = ('-created_at',)

