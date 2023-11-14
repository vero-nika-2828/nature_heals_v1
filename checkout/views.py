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
        'order_form': order_form
    }
    return render(request, template, context)
