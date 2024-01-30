from django.shortcuts import render

def contact(request):
    """Returns index page"""
    return render(request, 'contact/contact.html')
