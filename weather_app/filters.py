"""Weather App Filters."""

from django_filters import BooleanFilter, CharFilter, NumberFilter
from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet, SearchFilter
from nautobot.extras.filters import NaturalKeyOrPKMultipleChoiceFilter

from weather_app import models


class WeatherFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Weather App Filter"""

    location = NaturalKeyOrPKMultipleChoiceFilter(queryset=models.Location.objects.all(), to_field_name="name")
    short_forecast = CharFilter(field_name="short_forecast", lookup_expr="icontains")
    temperature = NumberFilter(field_name="temperature", lookup_expr="icontains")
    probability_of_precipitation = NumberFilter(field_name="probability_of_precipitation", lookup_expr="icontains")
    relative_humidity = NumberFilter(field_name="relative_humidity", lookup_expr="icontains")
    wind_speed = CharFilter(field_name="wind_speed", lookup_expr="icontains")
    wind_direction = CharFilter(field_name="wind_direction", lookup_expr="icontains")
    is_severe = BooleanFilter(field_name="is_severe", label="Severe Weather")

    # Search Box
    q = SearchFilter(
        filter_predicates={
            "location__name": "icontains",
            "short_forecast": "icontains",
            "temperature": "icontains",
            "probability_of_precipitation": "icontains",
            "relative_humidity": "icontains",
            "wind_speed": "icontains",
            "wind_direction": "icontains",
        },
    )

    class Meta:
        """Meta attributes for filter."""

        model = models.Weather

        fields = [
            "location",
            "short_forecast",
            "temperature",
            "probability_of_precipitation",
            "relative_humidity",
            "wind_speed",
            "wind_direction",
        ]
