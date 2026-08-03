import django_filters

from .models import Job


class JobFilter(django_filters.FilterSet):

    min_salary = django_filters.NumberFilter(
        field_name="salary",
        lookup_expr="gte"
    )

    max_salary = django_filters.NumberFilter(
        field_name="salary",
        lookup_expr="lte"
    )

    min_cgpa = django_filters.NumberFilter(
        field_name="minimum_cgpa",
        lookup_expr="lte"
    )

    class Meta:
        model = Job

        fields = [
            "location",
            "job_type",
            "is_active",
        ]