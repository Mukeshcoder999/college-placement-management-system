from django.db import models
from django.conf import settings
# Create your models here.


class PlacementOfficerProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    employee_id = models.CharField(max_length=20, unique=True)

    phone = models.CharField(max_length=10)

    designation = models.CharField(max_length=100)

    office_address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username