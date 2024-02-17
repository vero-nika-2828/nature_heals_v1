from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from products.models import Product


def shopping_bag(request):
    """Display shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add the product to the shopping bag.
    Increment quantities of slected products
    """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'Updated {product.friendly_name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.friendly_name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """
    Change the product product quantity in shopping bag.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {product.friendly_name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(
            request,
            f'Removed {product.friendly_name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_bag_item(request, item_id):
    """
    Remove the product product quantity in shopping bag.
    """
    print("Posted to add to bag")
    print(item_id)
    # product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)
        print(product)
        bag.pop(item_id)
        messages.success(
            request,
            f'Removed {product.friendly_name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item:(e)')
        return HttpResponse(status=500)
