from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

def contact(request):
    """Render contact page"""
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request, f'Thank you for your message. \
                    We will get back to you as soon as we can.')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'It has not been possible to submit your message. \
                    Please check the form.')
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form,
    }
    
    return render(request, template, context)
