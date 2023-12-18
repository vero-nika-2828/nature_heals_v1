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
    if not request.user.is_authenticated:
        messages.error(request,'Log in to add your Wishlist.')
        return redirect(reverse('account_login'))
    
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
    if not request.user.is_authenticated:
        messages.error(request,'Log in to add your Wishlist.')
        return redirect(reverse('products'))

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # check whether the product is already in wishlist
    existing_wish_item = Wishlist.objects.filter(user_profile=user, product=product)
    
    # add a product to wishlist if not yet added
    if existing_wish_item:
        messages.info(request, f'{product.friendly_name} is already in your wishlist!')
        return redirect(reverse('products'))
    else:
        Wishlist.objects.create(
            user_profile=user,
            product=product,
    )

        messages.success(request, f'{product.friendly_name} has been added to your wishlist!')
        return redirect(reverse('products'))
 

def remove_from_wishlist(request, product_id):
    """
    Remove products from the wishlist
    """

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    wishlist_count = Wishlist.objects.count()

    Wishlist.objects.filter(user_profile=user, product=product).delete()

    previous_url = request.META.get('HTTP_REFERER')
    previous_url_link = [x for x in previous_url]
    final_url = previous_url_link[-9]+previous_url_link[-8]+previous_url_link[-7]+previous_url_link[-6]+previous_url_link[-5]+previous_url_link[-4]+previous_url_link[-3]+previous_url_link[-2]

    if final_url == 'products':
       return redirect(reverse('products'))
    else:
       return redirect(reverse('wishlist'))