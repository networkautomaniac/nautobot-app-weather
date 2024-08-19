from django.db import models

from nautobot.apps.models import PrimaryModel, extras_features


@extras_features("graphql")
class Weather(PrimaryModel):
    """Model for weather."""

    location = models.OneToOneField(to="dcim.location", on_delete=models.CASCADE)
    short_forecast = models.CharField(verbose_name="Short Forecast", max_length=255)
    temperature = models.IntegerField(verbose_name="Temperature")
    probability_of_precipitation = models.IntegerField(verbose_name="Probability of Precipitation")
    relative_humidity = models.IntegerField(verbose_name="Relative Humidity")
    wind_speed = models.CharField(verbose_name="Wind Speed", max_length=255)
    wind_direction = models.CharField(verbose_name="Wind Direction", max_length=255)

    @property
    def is_severe(self):
        return "severe" in self.short_forecast.lower()
