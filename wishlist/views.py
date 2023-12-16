from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
# from wishlist.models import WishList


def wishlist(request):

    template = 'wishlist/my_wishlist.html'

    return render(request, template)
