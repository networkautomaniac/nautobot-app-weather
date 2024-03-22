"""App declaration for weather."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import ConstanceConfigItem, NautobotAppConfig

__version__ = metadata.version(__name__)


class WeatherConfig(NautobotAppConfig):
    """App configuration for the weather app."""

    name = "weather"
    verbose_name = "Weather"
    version = __version__
    author = "Aaron Britton"
    description = "Weather."
    base_url = "weather"
    required_settings = []
    min_version = "2.1.7"
    max_version = "2.9999"
    default_settings = {}

    constance_config = {
        "ENABLE_JOB": ConstanceConfigItem(field_type=bool, default=True, help_text="Enable Job."),
    }

    def ready(self):
        super().ready()

        from nautobot.core.signals import nautobot_database_ready
        from weather.signals import create_location_custom_field, enable_job, schedule_job

        nautobot_database_ready.connect(create_location_custom_field, sender=self)
        nautobot_database_ready.connect(enable_job, sender=self)
        nautobot_database_ready.connect(schedule_job, sender=self)


config = WeatherConfig  # pylint:disable=invalid-name
