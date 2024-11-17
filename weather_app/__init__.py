"""App declaration for weather_app."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig, ConstanceConfigItem

__version__ = metadata.version(__name__)


class WeatherAppConfig(NautobotAppConfig):
    """App configuration for the weather_app app."""

    name = "weather_app"
    verbose_name = "Weather App"
    version = __version__
    author = "Aaron Britton"
    description = "Weather App."
    base_url = "weather-app"
    required_settings = []
    min_version = "2.3"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}
    docs_view_name = "plugins:weather_app:docs"

    constance_config = {
        "ENABLE_JOB": ConstanceConfigItem(field_type=bool, default=True, help_text="Enable Job."),
    }

    def ready(self):
        super().ready()

        from nautobot.core.signals import nautobot_database_ready
        from weather_app.signals import create_location_custom_field, enable_job, schedule_job

        nautobot_database_ready.connect(create_location_custom_field, sender=self)
        nautobot_database_ready.connect(enable_job, sender=self)
        nautobot_database_ready.connect(schedule_job, sender=self)


config = WeatherAppConfig  # pylint:disable=invalid-name
