"""API serializers for weather_app."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from weather_app import models


class WeatherSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """Weather Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.Weather
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
