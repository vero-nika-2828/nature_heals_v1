from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

        review = forms.CharField(
            widget=forms.Textarea(attrs={
                            'rows': '4',
                            'placeholder': 'Write your review here'})
        )

    def __init__(self, *args, **kwargs):
        # Call default django form
        super().__init__(*args, **kwargs)
  

  
        # Customize fields
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            
           

