import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    cart_items = []
    order = {'order_total_price': 0, 'order_item_quantity': 0}

    for ItemColor_id in cart:
        color_code = cart[ItemColor_id]['color']
        quantity = cart[ItemColor_id]['quantity']
        color = Color.objects.get(color=color_code)
        item_color = ItemColor.objects.get(id=ItemColor_id)
        cart_item = item_color.item

        order_item_price = cart_item.price * int(quantity)
        order['order_total_price'] += order_item_price
        order['order_item_quantity'] += int(quantity)

        cart_item_info = {
            'item':{
                'id': ItemColor_id,
                'name': cart_item.name,
                'vendor': cart_item.vendor_name,
                'color': color.name,
                'color_code': color_code,
                'price': cart_item.price,
                'imageURL': cart_item.imageitem_set.first().image.name
            },
            'quantity': quantity,
            'available': item_color.quantity,
            'total_price': order_item_price 
        }

        cart_items.append(cart_item_info)

    return {'cart_items': cart_items, 'cart_order': order}

def cookieData(request):
    cookieData = cookieCart(request)

    cart_items = cookieData['cart_items']
    cart_order = cookieData['cart_order']

    context = {
        'order': cart_order,
        'items': cart_items
    }

    return context