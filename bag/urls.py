from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('edit/<item_id>/', views.edit_bag, name='edit_bag'),
    path('remove/<item_id>/', views.remove_bag_item, name='remove_bag_item'),
]
