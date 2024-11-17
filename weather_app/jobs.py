"""Weather App Jobs."""

from nautobot.apps.jobs import Job, register_jobs
from nautobot.dcim.models import Location

from weather_app.models import Weather
from weather_wise.weather_wise import WeatherWise


class UpdateLocationWeather(Job):
    class Meta:
        name = "Update Location Weather"
        description = "Get weather related details based on zipcode for a location."
        has_sensitive_variables = False

    def run(self):
        for location in Location.objects.all():

            # Get CustomField "zipcode" from Location.
            zipcode = location.cf.get("zipcode")
            if zipcode:
                weather = WeatherWise(zipcode)

                # Update or create Weather object.
                Weather.objects.update_or_create(
                    location=location,
                    defaults={
                        "short_forecast": weather.get_short_forecast(),
                        "temperature": weather.get_temperature_in_fahrenheit(),
                        "probability_of_precipitation": weather.get_probability_of_precipitation(),
                        "relative_humidity": weather.get_relative_humidity(),
                        "wind_speed": weather.get_wind_speed(),
                        "wind_direction": weather.get_wind_direction(),
                    },
                )


register_jobs(UpdateLocationWeather)
