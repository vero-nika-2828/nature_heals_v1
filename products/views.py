from django.shortcuts import render


def products(request):
    """Returns products page"""

    return render(request, 'products/product.html')
