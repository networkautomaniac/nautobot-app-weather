from nautobot.apps.jobs import Job, register_jobs
from nautobot.dcim.models import Location

from weather.models import Weather
from weather_wise.weather_wise import WeatherWise


class UpdateLocationWeather(Job):
    class Meta:
        name = "Update Location Weather"
        description = "This job gets weather related details based on zipcode for a location."
        has_sensitive_variables = False

    def run(self):
        for location in Location.objects.all():
            # Get CustomField "zipcode" from Location.
            zipcode = location.cf.get("zipcode")
            if zipcode:
                weather = WeatherWise(zipcode)
                short_forecast = weather.get_short_forecast()
                temperature_in_fahrenheit = weather.get_temperature_in_fahrenheit()
                probability_of_precipitation = weather.get_probability_of_precipitation()
                wind = weather.get_wind()

                Weather.objects.update_or_create(
                    location=location,
                    defaults={
                        "short_forecast": short_forecast,
                        "temperature": temperature_in_fahrenheit,
                        "probability_of_precipitation": probability_of_precipitation,
                        "wind": wind,
                    },
                )


register_jobs(UpdateLocationWeather)
