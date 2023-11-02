from django.contrib import admin

from apps.products.models import ProductsModel

# Register your models here.
class ProductsModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProductsModel, ProductsModelAdmin)