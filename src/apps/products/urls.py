from django.urls import path

from apps.products.views import ScrapeView

urlpatterns = [
    path("product/scrape/", ScrapeView.as_view(),name="scrape-product")
]