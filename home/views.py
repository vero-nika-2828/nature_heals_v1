from django.shortcuts import render
from django.db.models import F
from products.models import Product


def index(request):
    """Returns index page"""
    popular_products = (
        Product.objects.filter(featured=True).exclude(image='').order_by('?')[:4])

    context = {
        'popular_products': popular_products,
    }

    return render(request, 'home/index.html', context)
