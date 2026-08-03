from django.db import models
from django.conf import settings

# Create your models here.

class StudentProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()

    college_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    passing_year = models.IntegerField()

    cgpa = models.DecimalField(max_digits=4, decimal_places=2)

    address = models.TextField()

    resume = models.FileField(upload_to='resumes/', blank = True, null = True)
    profile_picture = models.ImageField(upload_to='profile_pictures/')

    skills = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username