from nautobot.apps.ui import TemplateExtension

from weather.models import Weather


class LocationWeatherPanel(TemplateExtension):
    """Add the weather panel to locations on the right side of the page."""

    model = "dcim.location"

    def right_page(self):

        # Try to store an instance of weather context for location.  This is needed to prevent the page rendering from breaking.
        # try:
        #     weather = Weather.objects.get(location=self.context["object"])
        # except Weather.DoesNotExist:
        #     weather = None

        # Render the weather_panel.html along with extra_context which displays the actual values.
        return self.render(
            "weather/weather_panel.html",
            # extra_context={
            #     "weather": weather,
            # },
        )


template_extensions = [LocationWeatherPanel]
