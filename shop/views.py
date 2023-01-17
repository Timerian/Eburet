from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings

import json

from .models import *

from .utils import cookieData


def main(request):
    context = {}
    return render(request, "shop/main.html")

def itemList(request):
    items = Item.objects.all()

    context = cookieData(request)
    context['items'] = items
    return render(request, "shop/store.html", context)


def itemDetail(request, id):
    item = Item.objects.get(id=id)

    context = cookieData(request)
    context['item'] = item
    return render(request, 'shop/item.html', context)

@ensure_csrf_cookie
def updateItem(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    action = data['action']
    color = data['color']
    # quantity = data['quantity']

    itemColor = ItemColor.objects.get(item=item_id, color=Color.objects.get(color=color))

    session = request.session
    order = session.get(settings.CART_SESSION_ID)
    if not order:
        order = session[settings.CART_SESSION_ID] = Order.objects.create()
        orderItem = OrderItem.objects.create(order=order, item=itemColor)

    # if action == 'add':
    #     orderItem.quantity = (orderItem.quantity + quantity)

    print('Action:', action)
    print('Item ID:', item_id)



    return JsonResponse('Item added', safe=False)

def creatingOrder(request):
    data = json.loads(request.body)
    return JsonResponse('Payment complete...')

def about(request):
    context = {}
    return render(request, "shop/about.html", context)

def contacts(request):
    context = {}
    return render(request, "shop/contacts.html", context)

def help(request):
    context = {}
    return render(request, "shop/help.html", context)

def updateContext(request):
    print(json.loads(request.COOKIES['cart']))
    context = cookieData(request)
    return render(request, 'shop/cart.html', context)