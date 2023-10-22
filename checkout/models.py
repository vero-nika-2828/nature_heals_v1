import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    """
    Order model  to store orders
    Contains unique and permanent order number
    """

    order_number = models.CharField(max_length=35, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=60, null=False, blank=False)
    street_address2 = models.CharField(max_length=60, null=True, blank=True)
    county = models.CharField(max_length=60, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=12, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=12, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
 

