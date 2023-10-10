from django.shortcuts import render
from .models import Product


def all_products(request):
    """Return products page and display all products, search and sort results"""

    products = Product.objects.all()

    context = {
        "products": products,
    }
    return render(request, 'products/products.html', context)
