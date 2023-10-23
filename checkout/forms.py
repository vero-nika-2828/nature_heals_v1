from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        # Call default django form
        super().__init__(*args, **kwargs)
        # Form placeholders list
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Place cursor in full name field when page loads
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # Customize fields
        for field in self.fields:
            # Add asterisk to required fields
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                # Add placeholder name
                placeholder = placeholders[field]
            # Other fields customization
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
