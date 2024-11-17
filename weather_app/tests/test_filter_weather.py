"""Test Weather Filter."""

from django.test import TestCase

from weather_app import filters, models
from weather_app.tests import fixtures


class WeatherFilterTestCase(TestCase):
    """Weather Filter Test Case."""

    queryset = models.Weather.objects.all()
    filterset = filters.WeatherFilterSet

    @classmethod
    def setUpTestData(cls):
        """Setup test data for Weather Model."""
        fixtures.create_weather()

    def test_q_search_name(self):
        """Test using Q search with name of Weather."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for Weather."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
