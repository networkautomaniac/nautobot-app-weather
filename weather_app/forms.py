"""Weather App Forms."""

from django import forms
from nautobot.apps.forms import (
    NautobotBulkEditForm,
    NautobotFilterForm,
    NautobotModelForm,
    TagsBulkEditFormMixin,
    DynamicModelMultipleChoiceField,
    StaticSelect2,
)
from nautobot.core.forms.constants import BOOLEAN_WITH_BLANK_CHOICES
from weather_app import models


# Unused.  Weather isn't added or edited manually.  Removed "Add Weather" button from the UI in views.py.
class WeatherForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """Weather App Create/Edit Form."""

    # location = DynamicModelMultipleChoiceField(
    #     required=False,
    #     label="Location",
    #     queryset=models.Location.objects.all(),
    # )
    # short_forecast = forms.CharField(required=False, label="Short Forecast")
    # temperature = forms.IntegerField(required=False, label="Temperature")
    # probability_of_precipitation = forms.IntegerField(required=False, label="Probability of Precipitation")
    # relative_humidity = forms.IntegerField(required=False, label="Relative Humidity")
    # wind_speed = forms.CharField(required=False, label="Wind Speed")
    # wind_direction = forms.CharField(required=False, label="Wind Direction")
    # is_severe = forms.NullBooleanField(
    #     required=False,
    #     label="Severe Weather",
    #     widget=StaticSelect2(choices=BOOLEAN_WITH_BLANK_CHOICES),
    # )

    class Meta:
        """Meta Attributes."""

        model = models.Weather
        fields = [
            # "location",
            # "short_forecast",
            # "temperature",
            # "probability_of_precipitation",
            # "relative_humidity",
            # "wind_speed",
            # "wind_direction",
        ]


# Unused.  Weather isn't bulk added or bulk edited manually.
class WeatherBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """Weather App Bulk Edit Form."""

    # location = DynamicModelMultipleChoiceField(
    #     required=False,
    #     label="Location",
    #     queryset=models.Location.objects.all(),
    # )
    # short_forecast = forms.CharField(required=False, label="Short Forecast")
    # temperature = forms.IntegerField(required=False, label="Temperature")
    # probability_of_precipitation = forms.IntegerField(required=False, label="Probability of Precipitation")
    # relative_humidity = forms.IntegerField(required=False, label="Relative Humidity")
    # wind_speed = forms.CharField(required=False, label="Wind Speed")
    # wind_direction = forms.CharField(required=False, label="Wind Direction")
    # is_severe = forms.NullBooleanField(
    #     required=False,
    #     label="Severe Weather",
    #     widget=StaticSelect2(choices=BOOLEAN_WITH_BLANK_CHOICES),
    # )

    class Meta:
        """Meta Attributes."""

        model = models.Weather
        fields = [
            # "location",
            # "short_forecast",
            # "temperature",
            # "probability_of_precipitation",
            # "relative_humidity",
            # "wind_speed",
            # "wind_direction",
        ]


class WeatherFilterForm(NautobotFilterForm):  # pylint: disable=too-many-ancestors
    """Weather App Filter Form.."""

    model = models.Weather

    # Filter Fields
    location = DynamicModelMultipleChoiceField(
        required=False,
        label="Location",
        queryset=models.Location.objects.all(),
    )
    short_forecast = forms.CharField(required=False, label="Short Forecast")
    temperature = forms.IntegerField(required=False, label="Temperature")
    probability_of_precipitation = forms.IntegerField(required=False, label="Probability of Precipitation")
    relative_humidity = forms.IntegerField(required=False, label="Relative Humidity")
    wind_speed = forms.CharField(required=False, label="Wind Speed")
    wind_direction = forms.CharField(required=False, label="Wind Direction")
    # is_severe = forms.NullBooleanField(
    #     required=False,
    #     label="Severe Weather",
    #     widget=StaticSelect2(choices=BOOLEAN_WITH_BLANK_CHOICES),
    # )

    # Filter Button Field Order
    field_order = [
        "location",
        "short_forecast",
        "temperature",
        "probability_of_precipitation",
        "relative_humidity",
        "wind_speed",
        "wind_direction",
    ]
