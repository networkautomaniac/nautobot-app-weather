"""Signals for Weather App.

Note that we can't directly import models here as this signal callback happens during the post-migrate state. Hence,
the apps.get_model calls everywhere.
"""

from datetime import datetime, timedelta
from constance import config
from django.contrib.auth import get_user_model
from nautobot.extras.models import Job, ScheduledJob
from nautobot.extras.choices import JobExecutionType
from weather_app.jobs import UpdateLocationWeather


def create_location_custom_field(apps, **kwargs):
    """Create a custom field (zipcode) for locations."""

    # Use `apps.get_model()` to look up Nautobot core models.
    CustomField = apps.get_model("extras", "CustomField")
    ContentType = apps.get_model("contenttypes", "ContentType")
    Location = apps.get_model("dcim", "Location")

    # Get the Location ContentType
    location_content_type = ContentType.objects.get_for_model(Location)

    custom_field, _ = CustomField.objects.update_or_create(
        defaults={
            "label": "Zipcode",
            "key": "zipcode",
            "type": "text",
            "weight": "100",
            "filter_logic": "loose",
            "validation_regex": "^\d{5}$",
        },
    )
    # Set the ContentType
    custom_field.content_types.set([location_content_type])

    return custom_field


def enable_job(apps, **kwargs):
    """Enable the Weather app job."""

    if config.weather_app__ENABLE_JOB:
        for job in Job.objects.filter(module_name__startswith="weather_app.jobs"):
            job.enabled = True
            job.validated_save()


def schedule_job(apps, **kwargs):
    """Schedule the Weather app job."""

    # Adjust time to start at the top of the hour.
    start_time = datetime.now()
    start_time = start_time.replace(minute=0) + timedelta(hours=1)

    ScheduledJob.objects.update_or_create(
        name="Hourly Location Weather Update",
        task=f"{UpdateLocationWeather.__module__}.{UpdateLocationWeather.__name__}",  # "weather_app.jobs.UpdateLocationWeather
        defaults={
            "job_model": Job.objects.get(
                job_class_name=UpdateLocationWeather.__name__, module_name=UpdateLocationWeather.__module__
            ),
            "enabled": True,
            "user": get_user_model().objects.get(username="admin"),
            "start_time": start_time,
            "description": "Updates a locations weather every hour.",
            "interval": JobExecutionType.TYPE_HOURLY,
        },
    )
