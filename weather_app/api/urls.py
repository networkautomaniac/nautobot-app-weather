"""Django API urlpatterns declaration for weather_app app."""

from nautobot.apps.api import OrderedDefaultRouter

from weather_app.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("weather", views.WeatherViewSet)

urlpatterns = router.urls
