from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from typing import Any

from apps.products.models import ProductsModel
from apps.products.serializers import ProductModelSerializer
from services.scraper.runner import Runner

class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = ProductsModel.objects.all()

    def list(self, request, *args, **kwargs):
        # Mengambil data produk dari basis data
        products = self.queryset
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)

    # running the scraper method
    def create(self, request, *args, **kwargs):

        # define keyword
        query: str = request.data.get("query")
        page_number: str = request.data.get("page", "1")

        # define scraper
        scraper: Runner = Runner()
        product_data: list[dict[str, Any]] = scraper.search_product(keyword=query, page_number=page_number)
        
        serializer = self.get_serializer(data=product_data)

        # data validation
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return super().create(request, *args, **kwargs)