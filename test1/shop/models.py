from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=7, verbose_name="Цена")
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_preview")
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
