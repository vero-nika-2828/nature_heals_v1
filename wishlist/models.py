from django.db import models

from profiles.models import UserProfile
from products.models import Product

class Wishlist(models.Model):
    """
    Wishlist model to show products shortlisted by user
    """

    wishlist_username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'WishList ({self.user_profile})'