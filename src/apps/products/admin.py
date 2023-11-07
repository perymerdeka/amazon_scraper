from django.contrib import admin

from apps.products.models import ProductsModel

# Register your models here.
class ProductsModelAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

admin.site.register(ProductsModel, ProductsModelAdmin)