"""Weather App Tables."""

import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, ToggleColumn, BooleanColumn

from weather_app import models


class WeatherTable(BaseTable):  # pylint: disable=R0903
    """Weather App Table."""

    pk = ToggleColumn()
    location = tables.LinkColumn()
    short_forecast = tables.Column()
    temperature = tables.Column()
    probability_of_precipitation = tables.Column()
    relative_humidity = tables.Column()
    wind_speed = tables.Column()
    wind_direction = tables.Column()
    is_severe = BooleanColumn(verbose_name="Severe Weather", orderable=False)

    # Removed "Edit" Option.
    actions = ButtonsColumn(models.Weather, buttons=("changelog", "delete"))

    class Meta(BaseTable.Meta):
        """Meta Attributes."""

        model = models.Weather
        fields = (
            "pk",
            "location",
            "short_forecast",
            "temperature",
            "probability_of_precipitation",
            "relative_humidity",
            "wind_speed",
            "wind_direction",
            "is_severe",
            "actions",
        )

        default_columns = (
            "pk",
            "location",
            "short_forecast",
            "temperature",
            "probability_of_precipitation",
            "relative_humidity",
            "wind_speed",
            "wind_direction",
            "is_severe",
            "actions",
        )
