function updateCartItemInfo(itemColor_Id, action, color, quantity, cart, price){
    var status = addCookieItem(itemColor_Id, action, color, quantity)
    setItemQuantity(cart)
    setTotalPrice(cart)
    document.querySelector('span.badge').textContent = getTotalItemQuantity(cart)

    if (status == 'deleted'){
        var list_item_id = '#mw-list-item' + itemColor_Id
        document.querySelector(list_item_id).remove()
        return
    }

    var btnId = '#quantity' + itemColor_Id
    document.querySelector(btnId).textContent = cart[itemColor_Id]['quantity']

    var priceId = '#price' + itemColor_Id
    document.querySelector(priceId).textContent = (cart[itemColor_Id]['quantity'] * price) + 'р.'
}

function cartBtnsListener(){
    var cartBtns = document.getElementsByClassName('mw-cart-btn')

    for (var i = 0; i < cartBtns.length; i++){
        cartBtns[i].addEventListener('click', function(){
            var action = this.dataset.action
            var color = this.dataset.color
            var itemColor_Id = this.dataset.itemcolorid
            var price = cart[itemColor_Id]['price']
            var quantity = 1

            updateCartItemInfo(itemColor_Id, action, color, quantity, cart, price)
            }
        )
    }

}

cartBtnsListener()