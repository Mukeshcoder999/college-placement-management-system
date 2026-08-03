from django.db import models
from django.conf import settings

# Create your models here.

class CompanyProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(max_length=150)

    company_email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10)

    website = models.URLField(blank=True, null=True)

    address = models.TextField()

    description = models.TextField()

    logo = models.ImageField(
        upload_to='company_logos/',
        blank=True,
        null=True
    )

    established_year = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name