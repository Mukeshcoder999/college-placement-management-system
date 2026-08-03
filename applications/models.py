from django.db import models
from students.models import StudentProfile
from jobs.models import Job

# Create your models here.

class JobApplication(models.Model):

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    ]

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    application_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    def __str__(self):
        return f"{self.student.user.username} - {self.job.job_title}"