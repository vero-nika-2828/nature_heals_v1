from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    Return products page and display all products, search and sort results
    """
    # Retrieve Product model data
    products = Product.objects.all()
    search_word = None

    if request.GET:
        if 'search' in request.GET:
            # Get the term entered in the search bar
            search_word = request.GET['search']
            # Prompt the user to enter the search word if none was entered
            if not search_word:
                messages.error(request, "Did you enter a searh word?")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=search_word) | Q(
                    description__icontains=search_word) | Q(
                        full_ingredients__icontains=search_word) | Q(
                            healing_properties__icontains=search_word)

            products = products.filter(queries)

    context = {
        "products": products,
        "seach_word": search_word,
    }
    return render(request, 'products/products.html', context)
