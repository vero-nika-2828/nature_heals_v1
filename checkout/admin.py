from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    # Enable use of OrderLineItem model within Order Model
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # Access OrderLineItem model from Order
    inlines = (OrderLineItemAdminInline,)

    """
    Set fields where values are calculated by model method to read only to
    disable the possibilit of editing
    """
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',)

    """
    Order the fields to match the order in the model
    Override default django order specified for readonly fields
    """
    fields = (
        'order_number',
        'user_profile'
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county', 'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )

    # Show only selected key columns in the order list
    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total',)

    # Order by date, most recent orders first
    ordering = ('-date',)


# Register models
admin.site.register(Order, OrderAdmin)
