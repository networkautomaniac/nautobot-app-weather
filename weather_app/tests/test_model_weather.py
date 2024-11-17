"""Test Weather."""

from django.test import TestCase

from weather_app import models


class TestWeather(TestCase):
    """Test Weather."""

    def test_create_weather_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        weather = models.Weather.objects.create(name="Development")
        self.assertEqual(weather.name, "Development")
        self.assertEqual(weather.description, "")
        self.assertEqual(str(weather), "Development")

    def test_create_weather_all_fields_success(self):
        """Create Weather with all fields."""
        weather = models.Weather.objects.create(name="Development", description="Development Test")
        self.assertEqual(weather.name, "Development")
        self.assertEqual(weather.description, "Development Test")
