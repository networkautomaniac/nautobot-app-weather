"""Test weather forms."""

from django.test import TestCase

from weather_app import forms


class WeatherTest(TestCase):
    """Test Weather forms."""

    def test_specifying_all_fields_success(self):
        form = forms.WeatherForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.WeatherForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_weather_is_required(self):
        form = forms.WeatherForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
