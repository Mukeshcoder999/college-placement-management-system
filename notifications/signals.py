from django.db.models.signals import post_save
from django.dispatch import receiver

from applications.models import JobApplication
from .models import Notification


@receiver(post_save, sender=JobApplication)
def notify_company_on_new_application(sender, instance, created, **kwargs):

    if created:

        Notification.objects.create(
            recipient=instance.job.company.user,
            title="New Job Application",
            message=(
                f"{instance.student.user.username} "
                f"applied for "
                f"{instance.job.job_title}."
            )
        )