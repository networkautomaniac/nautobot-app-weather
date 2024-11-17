"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from weather_app import models
from weather_app.tests import fixtures


class WeatherViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the Weather views."""

    model = models.Weather
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_weather()
