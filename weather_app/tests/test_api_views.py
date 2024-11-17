"""Unit tests for weather_app."""

from nautobot.apps.testing import APIViewTestCases

from weather_app import models
from weather_app.tests import fixtures


class WeatherAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for Weather."""

    model = models.Weather
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_weather()
