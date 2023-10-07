from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Category model for available product categories
    """

    name = models.CharField(
        max_length=254)
    friendly_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subcategory(models.Model):
    """
    Subategory model for available product subcategories
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Product model for all products.
    """
    name = models.CharField(
        max_length=254)
    friendly_name = models.CharField(
        max_length=254)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(
        Subcategory, null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254)
    size = models.CharField(
        max_length=254, null=True, blank=True)
    description = models.TextField()
    healing_properties = models.CharField(
        max_length=254, null=True, blank=True)
    herbal_ingredients = models.CharField(
        max_length=254, null=True, blank=True)
    vitamins_minerals = models.CharField(
        max_length=254, null=True, blank=True)
    full_ingredients = models.CharField(
        max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(
         max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
 