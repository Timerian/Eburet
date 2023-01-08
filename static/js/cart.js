var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var item_id = this.dataset.item
        var action = this.dataset.action
        selectColor = document.querySelector('input[name="radio"]:checked')
        var color = selectColor.dataset.color
        console.log('item_id', item_id, 'action', action, 'color', color)   
        addCookieItem(item_id, action)
    })
}

function addCookieItem(item_id, action) {
    console.log(cart)
    if (action == 'add'){
        if (cart[item_id] == undefined){
            cart[item_id] = {'quantity': 1}
        }else{
            cart[item_id]['quantity'] += 1
        }
        console.log('Item added')
    }

    if (action == 'remove'){
        cart[item_id]['quantity'] -= 1

        if (cart[item_id]['quantity'] <= 0){
            delete cart[item_id]
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