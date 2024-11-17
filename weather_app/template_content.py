from nautobot.apps.ui import TemplateExtension


class LocationWeatherPanel(TemplateExtension):
    """Add a weather panel to a location on the right side of the page."""

    model = "dcim.location"

    def right_page(self):
        return self.render(
            "weather_app/weather_panel.html",
        )


template_extensions = [LocationWeatherPanel]
