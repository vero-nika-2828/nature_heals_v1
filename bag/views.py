from django.shortcuts import render, redirect, reverse


def shopping_bag(request):
    """Display shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add the product to the shopping bag.
    Increment quantities of slected products
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """
    Change the product product quantity in shopping bag.
    """

    quantity = int(request.POST.get('quantity'))

    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] += quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_bag_item(request, item_id):
    product = get_object_or_404(Product, pk=item_id)

    try:
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except EXCEPTION as e:
        return HttpResponse(status=500)
