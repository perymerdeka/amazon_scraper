from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from typing import Any

from apps.products.models import ProductsModel
from apps.products.serializers import ProductModelSerializer
from services.scraper.runner import Runner

class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = ProductsModel.objects.all()

    # membuat fitur search
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.query_params.get('search', None)

        if query:
            # Customize this based on your model fields
            queryset = queryset.filter(title__icontains=query)
        
        return queryset

    def list(self, request, *args, **kwargs):
        # Mengambil data produk dari basis data
        products = self.queryset
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)



