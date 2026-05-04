from django.urls import path
from .views import SalesForecastView

urlpatterns = [
    path("forecast/", SalesForecastView.as_view(), name="forecast"),
]