from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    display = {
        'user_profile',
        'product',
        'review',
        'review_date',

    }

    ordering = ('review_date',)

admin.site.register(Review, ReviewAdmin)

