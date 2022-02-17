from django.db import models

# Create your models here.
from shop.models import Product


class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name