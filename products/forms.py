from django import forms
from django.http import request, HttpRequest
from .widgets import CustomClearableFileInput
from .models import Category, Subcategory, Product


class CategoryForm(forms.ModelForm):
    """
    Category form to enable adding categories
    """

    class Meta:
        """Set fields from category model"""
        model = Category
        fields = '__all__'

        image = forms.ImageField(label='Image', required=False,
                                 widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'friendly_name': 'Friendly Name',
            'name': 'Name',

        }

        self.fields['friendly_name'].widget.attrs['autofocus'] = True
        for field in self.fields:

            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class SubcategoryForm(forms.ModelForm):
    """
    Subcategory form to enable adding subcategories
    """

    class Meta:
        """Set fields from category model"""
        model = Subcategory
        fields = '__all__'

        image = forms.ImageField(label='Image', required=False,
                                 widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'friendly_name': 'Friendly Name',
            'name': 'Name',

        }

        self.fields['friendly_name'].widget.attrs['autofocus'] = True
        for field in self.fields:

            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class ProductForm(forms.ModelForm):
    """
    Produc form to enable adding products
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()

        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_subcategory = [(s.id, s.get_friendly_name()) for s in subcategories]

        self.fields['category'].choices = friendly_names
        self.fields['subcategory'].choices = friendly_names_subcategory

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'product-input-styling'
