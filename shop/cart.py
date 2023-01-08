from decimal import Decimal
from django.conf import settings
from .models import ItemColor, Item


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, orderItem, update_quantity=False):
        orderItem_id = str(orderItem.id)

        if orderItem_id not in self.cart:
            self.cart[item_id] = {'quantity': 0, 'total_price': 0}
        
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity

        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметка о том, что сессия была изменена 
        self.session.modified = True


    def remove(self, itemcolor):
        item_id = str(itemcolor.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save


    def __iter__(self):
        item_ids = self.cart.keys()
        items = ItemColor.objects.filter(id__in=item_ids)
        
        for item in items:
            item_id = str(item.id)
            self.cart[item_id]['item'] = item
            price = item.item.price
            self.cart[item_id]['total_price'] = self.cart[item_id]['quantity'] * price

    
    def __len__(self):
        return sum(value['quantity'] for value in self.cart.values())

    
    def get_total_price(self):
        return sum(Decimal(value['total_price']) for value in self.cart.values())


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

