from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Subcategory, Category
from profiles.models import UserProfile
from wishlist.models import Wishlist
from reviews.models import Review
from reviews.forms import ReviewForm


def all_products(request):
    """
    Display products page and display all products, search and sort results
    """
    # Retrieve Product model data
    products = Product.objects.all()
    search_word = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        if 'subcategory' in request.GET:
            # Filter products for selected subcategories
            subcategories = request.GET['subcategory'].split(',')
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if 'sort' in request.GET:
            # Sort the producutcs per specified criteria
            sort_preference = request.GET['sort']
            sort = sort_preference
            if sort_preference == 'name':
                sort_preference == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sort_preference == 'category':
                sort_preference = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sort_preference = f'-{sort_preference}'
            products = products.order_by(sort_preference)

        if 'search' in request.GET:
            # Get the term entered in the search bar
            search_word = request.GET['search']
            # Prompt the user to enter the search word if none was entered
            if not search_word:
                messages.error(request, "Did you enter a searh word?")
                return redirect(reverse('products'))
            # Search specification
            queries = Q(
                name__icontains=search_word) | Q(
                    description__icontains=search_word) | Q(
                        full_ingredients__icontains=search_word) | Q(
                            healing_properties__icontains=search_word)

            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    category_list = Category.objects.all()

    wishlist = None
    wishlist_product = None
    wishlist_product_list = None
    
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        wishlist = Wishlist.objects.filter(user_profile=user)
        wishlist_product = wishlist.values_list('product')
        wishlist_product_list = [x[0] for x in wishlist.values_list('product')]

    wishlist_count = Wishlist.objects.count()


    context = {
        'products': products,
        'search_word': search_word,
        'selected_subcategories': subcategories,
        'current_sorting': current_sorting,
        'category_list': category_list,
        'wishlist_count':wishlist_count,
        'wishlist_product_list': wishlist_product_list,
    }

    return render(request, 'products/products.html', context)




def product_details(request, product_id):
    """
    Display individual product page
    """
    product = get_object_or_404(Product, pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    healing_properties_list = product.healing_properties.split(",")
    
    reviews=None
    reviews = Review.objects.all()

    
    review_form = ReviewForm(request.POST)
    
    if request.method == "POST":
        if review_form.is_valid():
            reviews.create(
                user_profile=user_profile,
                product=product,
                review=request.POST.get('review'),
                review_date=request.POST.get('review_date'),
            )
            
            return redirect(reverse('product_details', args=[product_id]))
      
        else:
            review_form = ReviewForm()


    context = {
        'product': product,
        'healing_properties_list': healing_properties_list,
        'reviews':reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_details.html', context)
