from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from .models import Wishlist
# from wishlist.models import WishList


def wishlist(request):
    """
    Display my_wishlist page with the items selected by the user
    """
    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=user)

    template = 'wishlist/my_wishlist.html'

    context={
        'wishlist': wishlist,

    }
      
    return render(request, template, context)


def add_to_wishlist(request, product_id):
    """
    Add products to the wishlist
    """

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # check whether the product is already in wishlist
    existing_wish_item = Wishlist.objects.filter(user_profile=user, product=product)
    
    # add the product to wishlist if not yet added
    if existing_wish_item:
        # message.info(request, f'{product.name} is already in your wishlist!')
        return redirect(reverse('products'))
    else:
        Wishlist.objects.create(
            user_profile=user,
            product=product,
    )

    #message.success(
    #    request, f'{product.friendly_name} has been added to your wishlist!'
    #)

        return redirect(reverse('products'))
 

