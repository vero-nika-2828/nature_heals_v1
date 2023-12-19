from django.db import models

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """
    Revies model to store customer's reviews
    """
     
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=254)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_profile}"s review'