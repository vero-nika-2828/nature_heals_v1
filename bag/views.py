from django.shortcuts import render

""" Return shopping bag page """


def shopping_bag(request):
    return render(request, 'bag/bag.html')
