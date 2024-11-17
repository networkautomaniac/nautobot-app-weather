from django.contrib import admin
from nautobot.apps.admin import NautobotModelAdmin

from weather_app.models import Weather


@admin.register(Weather)
class WeatherAdmin(NautobotModelAdmin):
    list_display = (
        "location",
        "short_forecast",
        "temperature",
        "probability_of_precipitation",
        "relative_humidity",
        "wind_speed",
        "wind_direction",
        "is_severe",
    )
