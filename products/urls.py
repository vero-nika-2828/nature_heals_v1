from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_details, name='product_details'), 
    path('add_product/', views.add_product, name='add_product'), 
    path('edit_product/', views.edit_product, name='edit_product'),   
     
]
