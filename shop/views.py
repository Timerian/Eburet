from django.shortcuts import render


def main(request):
    context = {}
    return render(request, "shop/main.html")

def store(request):
    context = {}
    return render(request, "shop/store.html", context)

def cart(request):
    context = {}
    return render(request, "shop/cart.html", context)

def checkout(request):
    context = {}
    return render(request, "shop/checkout.html", context)

def about(request):
    context = {}
    return render(request, "shop/about.html", context)

def contacts(request):
    context = {}
    return render(request, "shop/contacts.html", context)

def help(request):
    context = {}
    return render(request, "shop/help.html", context)
