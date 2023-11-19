from django.urls import path

from apps.products.views import ScrapeView, ScrapeOnePageView

urlpatterns = [
    path("product/scrape/", ScrapeView.as_view(),name="scrape-product"),
    path("product/scrape-one-page/", ScrapeOnePageView.as_view(),name="scrape-one-product")
]