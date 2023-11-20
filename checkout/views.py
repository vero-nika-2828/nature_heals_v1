from django.shortcuts import render, redirect, reverse

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "Add items to your bag in order to proceed to checkout")
        return redirect(reverse('products'))

    order_form  = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OEUoTAFeUdFtYnWR4FaYZzkcirCDOPIKQBVjWM95VQUL4tGZRfMObfYSUEKKYkEABcLelhIYFvigrd6yCh82Jfe00ixbxnyoE',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
