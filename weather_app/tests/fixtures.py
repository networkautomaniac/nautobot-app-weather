"""Create fixtures for tests."""

from weather_app.models import Weather


def create_weather():
    """Fixture to create necessary number of Weather for tests."""
    Weather.objects.create(name="Test One")
    Weather.objects.create(name="Test Two")
    Weather.objects.create(name="Test Three")
