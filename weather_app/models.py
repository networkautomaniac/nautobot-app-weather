"""Weather App Model."""

from django.db import models
from nautobot.apps.models import PrimaryModel, extras_features
from nautobot.dcim.models import Location


@extras_features("graphql")
class Weather(PrimaryModel):  # pylint: disable=too-many-ancestors
    """Base model for Weather App."""

    location = models.OneToOneField(to="dcim.location", on_delete=models.CASCADE)
    short_forecast = models.CharField(verbose_name="Short Forecast", max_length=255)
    temperature = models.IntegerField(verbose_name="Temperature")
    probability_of_precipitation = models.IntegerField(verbose_name="Probability of Precipitation")
    relative_humidity = models.IntegerField(verbose_name="Relative Humidity")
    wind_speed = models.CharField(verbose_name="Wind Speed", max_length=255)
    wind_direction = models.CharField(verbose_name="Wind Direction", max_length=255)

    class Meta:
        """Meta class."""

        ordering = [
            "location",
            "short_forecast",
            "temperature",
            "probability_of_precipitation",
            "relative_humidity",
            "wind_speed",
            "wind_direction",
        ]

        # Option for fixing capitalization (i.e. "Snmp" vs "SNMP")
        # verbose_name = "Weather App"

        # Option for fixing plural name (i.e. "Chicken Tenders" vs "Chicken Tendies")
        # verbose_name_plural = "Weather Apps"

    # def __str__(self):
    #     """Stringify instance."""
    #     return self.location.name

    @property
    def is_severe(self):
        """
        Checks if the word "severe" is in the short forecast description.

        Returns:
            bool: True if "severe" is found in the short_forecast.  Otherwise, False.
        """
        return "severe" in self.short_forecast.lower()
