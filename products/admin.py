from django.contrib import admin
from .models import Product, Category, Subcategory

# Register your models


class ProductsAdmin(admin.ModelAdmin):
    display = {
        'name',
        'sku',
        'category',
        'subategory',
        'price',
        'image',
        'description',
    }


class CategoryAdmin(admin.ModelAdmin):
    display = {
        'name',
        'friendly_name',
    }


class SubcategoryAdmin(admin.ModelAdmin):
    display = {
        'name',
        'friendly_name',
    }


admin.site.register(Product, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
