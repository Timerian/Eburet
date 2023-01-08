import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    cart_items = []
    order = {'order_total_price': 0, 'order_item_quantity': 0}

    for item_id in cart:
        color_code = cart[item_id]['color']
        quantity = cart[item_id]['quantity']
        color = Color.objects.get(color=color_code)
        item_color = ItemColor.objects.get(item=item_id, color=color)
        cart_item = Item.objects.get(id=item_id)

        order_item_price = cart_item.price * quantity
        order['order_total_price'] += order_item_price
        order['order_item_quantity'] += quantity

        cart_item_info = {
            'item':{
                'id': cart_item.id,
                'name': cart_item.name,
                'vendor': cart_item.vendor_name,
                'color': color.name,
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