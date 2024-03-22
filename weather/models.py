from django.db import models

from nautobot.apps.models import PrimaryModel, extras_features


@extras_features("graphql")
class Weather(PrimaryModel):
    """Model for weather."""

    location = models.OneToOneField(to="dcim.location", on_delete=models.CASCADE)
    short_forecast = models.CharField(verbose_name="Short Forecast", max_length=255)
    temperature = models.IntegerField(verbose_name="Temperature")
    probability_of_precipitation = models.CharField(verbose_name="Probability of Precipitation", max_length=255)
    wind = models.CharField(verbose_name="Wind", max_length=255)
