function cartBtnsListener(){
    var cartBtns = document.getElementsByClassName('mw-cart-btn')

    for (var i = 0; i < cartBtns.length; i++){
        cartBtns[i].addEventListener('click', function(){
            var action = this.dataset.action
            var color = this.dataset.color
            var itemColor_Id = this.dataset.itemcolorid
            var price = cart[itemColor_Id]['price']

            if (action == 'add') {
                var quantity = 1
            } else if (action == 'remove') {
                var quantity = -1
                
                if (cart[itemColor_Id]['quantity'] == 1){
                    addCookieItem(itemColor_Id, action, color, quantity)
                    setItemQuantity(cart)
                    setTotalPrice(cart)
                    document.querySelector('span.badge').textContent = getTotalItemQuantity(cart)

                    var list_item_id = '#mw-list-item' + itemColor_Id
                    document.querySelector(list_item_id).remove()
                    return
                }
            }
            
            addCookieItem(itemColor_Id, action, color, quantity)

            setItemQuantity(cart)

            var btnId = '#quantity' + itemColor_Id
            document.querySelector(btnId).textContent = cart[itemColor_Id]['quantity']

            var priceId = '#price' + itemColor_Id
            document.querySelector(priceId).textContent = (cart[itemColor_Id]['quantity'] * price) + 'р.'

            setTotalPrice(cart)

            document.querySelector('span.badge').textContent = getTotalItemQuantity(cart)

            console.log('mw-cart-btn')
            }
        )
    }

}

cartBtnsListener()