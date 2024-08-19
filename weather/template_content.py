from nautobot.apps.ui import TemplateExtension


class LocationWeatherPanel(TemplateExtension):
    """Add a weather panel to locations on the right side of the page."""

    model = "dcim.location"

    def right_page(self):
        return self.render(
            "weather/weather_panel.html",
        )


template_extensions = [LocationWeatherPanel]
