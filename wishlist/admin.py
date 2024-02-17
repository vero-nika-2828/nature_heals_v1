from django.contrib import admin
from .models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    display = {
        'user_profile',
        'product',

    }


admin.site.register(Wishlist, WishlistAdmin)
