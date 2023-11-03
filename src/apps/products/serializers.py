from rest_framework.serializers import ModelSerializer

from apps.products.models import ProductsModel

class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'