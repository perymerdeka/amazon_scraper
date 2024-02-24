from django.db import models

# Create your models here.

class ProductsModel(models.Model):
    name = models.CharField(max_length=255)
    product_link = models.URLField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    uuid = models.UUIDField()
    asin = models.CharField(max_length=255)
    product_image_url = models.URLField()
    product_detail = models.TextField()

    def __str__(self) -> str:
        return "{}".format(self.name)