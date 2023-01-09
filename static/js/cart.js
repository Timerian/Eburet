var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        // var item_id = this.dataset.item
        var action = this.dataset.action

        selectColor = document.querySelector('input[name="radio"]:checked')
        var color = selectColor.dataset.color
        var itemColor_Id = selectColor.dataset.itemcolorid

        var quantity = document.querySelector('span.update-cart').textContent

        console.log('itemColor_Id', itemColor_Id, 'action', action, 'color', color, 'quantity', quantity)   
        addCookieItem(itemColor_Id, action, color, quantity)
    })
}

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

// function updateUserOrder(item_id, action, color){
//     console.log('Sending data...')

//     var url = "/update_item/"

//     console.log(csrftoken)

//     fetch(url, {
//         method: "POST",
//         headers: {
//             "Content-Type": "application/json",
//             "Accept": "application/json",
//             "X-CSRFToken": csrftoken
//         },
//         body: JSON.stringify({"item_id": item_id, "action": action, "color": color})
//     })
    
//     .then((response) => {
//         return response.json()
//     })

//     .then((data) => {
//         console.log('data', data)
//     })
// }