"""Weather App URLs."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter

from weather_app import views

router = NautobotUIViewSetRouter()
router.register("weather", views.WeatherUIViewSet)

# urlpatterns = [
#     path("docs/", RedirectView.as_view(url=static("weather_app/docs/index.html")), name="docs"),
# ]

# urlpatterns += router.urls
urlpatterns = router.urls
