from rest_framework.viewsets import ModelViewSet

from apps.products.models import ProductsModel
from apps.products.serializers import ProductModelSerializer

class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductModelSerializer
    queryset = ProductsModel.objects.all()