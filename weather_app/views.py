"""Weather App Views."""

from nautobot.apps.views import NautobotUIViewSet

from weather_app import filters, forms, models, tables
from weather_app.api import serializers


class WeatherUIViewSet(NautobotUIViewSet):
    """Weather App ViewSet."""

    bulk_update_form_class = forms.WeatherBulkEditForm
    filterset_class = filters.WeatherFilterSet
    filterset_form_class = forms.WeatherFilterForm
    form_class = forms.WeatherForm
    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer
    table_class = tables.WeatherTable

    # ObjectListViewMixin Override.  Remove Add, Edit & Export UI Button.
    action_buttons = ()
