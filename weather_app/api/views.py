"""API views for weather_app."""

from nautobot.apps.api import NautobotModelViewSet

from weather_app import filters, models
from weather_app.api import serializers


class WeatherViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """Weather viewset."""

    queryset = models.Weather.objects.all()
    serializer_class = serializers.WeatherSerializer
    filterset_class = filters.WeatherFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
