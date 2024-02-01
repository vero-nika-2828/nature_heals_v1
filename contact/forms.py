from django import forms
from django.http import request, HttpRequest
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Category form to enable user to send messages
    """

    class Meta:
        """Set fields from contact model"""
        model = Contact
        exclude = ('created_date',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full name',
            'email': 'Email',
            'message': 'What would you like to tell us?',

        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
    
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                   placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'contact-form-margin'
            self.fields[field].label = False

