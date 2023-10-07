from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name