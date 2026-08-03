from django.db import models
from companies.models import CompanyProfile
# Create your models here.

class Job(models.Model):

    JOB_TYPE = [
        ('Full Time', 'Full Time'),
        ('Internship', 'Internship'),
        ('Part Time', 'Part Time'),
    ]

    company = models.ForeignKey(
        CompanyProfile,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    job_title = models.CharField(max_length=150)

    description = models.TextField()

    required_skills = models.TextField()

    location = models.CharField(max_length=100)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    minimum_cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    vacancies = models.PositiveIntegerField()

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE
    )

    last_date = models.DateField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title