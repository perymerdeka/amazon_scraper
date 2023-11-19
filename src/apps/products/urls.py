from django.urls import path

from apps.products.views import ScrapeView, ScrapeOnePageView

urlpatterns = [
    path("products/scrape/", ScrapeView.as_view(),name="scrape-product"),
    path("products/scrape-one-page/", ScrapeOnePageView.as_view(),name="scrape-one-product")
]