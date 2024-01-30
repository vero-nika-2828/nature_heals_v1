from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    Contact model to submit customer's questions
    """

    name = models.CharField(max_length=35, null=True, blank=True)
    email =  models.EmailField(max_length=254)
    message = models.TextField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name}'


