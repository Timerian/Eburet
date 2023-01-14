// This script manage the logic of cart. 


// Getting total quantity of items in the cart
function getItemQuantity(cart){
    var Quantity = 0
    if (cart != {}){
        for (const key in cart){
            Quantity += parseInt(cart[key]['quantity']);
        }
    }
    return Quantity
}

// Setting value for the label indicating total item quantity in the cart (modal window)
function setItemQuantity(cart){
    var itemQuantity = getItemQuantity(cart)
    document.querySelector('span.cart-label').textContent = itemQuantity
}

// Updating cookie which contain cart information
function addCookieItem(itemColor_Id, action, color, quantity) {
    console.log(cart)
    if (action == 'add'){
        if (cart[itemColor_Id] == undefined){
            cart[itemColor_Id] = {'quantity': quantity, 'color': color}
        }else{
            cart[itemColor_Id]['quantity'] += quantity
        }
        console.log('Item added')
    }

    if (action == 'remove'){
        cart[itemColor_Id]['quantity'] -= 1

        if (cart[itemColor_Id]['quantity'] <= 0){
            delete cart[itemColor_Id]
        }
    }

    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
}

// Function for collecting information of items throught form on the item page.
// Also this function refresh cookie and cart label value.
function updateBtnsListener(){
    var updateBtns = document.getElementsByClassName('update-cart')

    for (var i = 0; i < updateBtns.length; i++){
        updateBtns[i].addEventListener('click', function(){
            // var item_id = this.dataset.item
            var action = this.dataset.action
            selectColor = document.querySelector('input[name="radio"]:checked')
            var color = selectColor.dataset.color
            var itemColor_Id = selectColor.dataset.itemcolorid
            var quantity = parseInt(document.querySelector('span.update-cart').textContent)
    
            console.log('itemColor_Id', itemColor_Id, 'action', action, 'color', color, 'quantity', quantity)   
            addCookieItem(itemColor_Id, action, color, quantity)
    
            setItemQuantity(cart)
        })
    }
}

updateBtnsListener()