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
    print(user)
    print(wishlist)
        

    return render(request, template, context)
