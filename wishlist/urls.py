from django.urls import path
from . import views

urlpatterns = [
     path('', views.wishlist, name='wishlist'),
   # path('<product_id>', views.product_details, name='product_details'),
   
]
