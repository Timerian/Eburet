from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def main(request):
    context = {}
    return render(request, "shop/main.html")

# def store(request):
#     context = {}
#     return render(request, "shop/store.html", context)


class ItemList(ListView):
    model = Item
    context_object_name = "items"
    template_name = "shop/store.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

        return context


class ItemDetail(DetailView):
    model = Item
    context_object_name = "item"
    template_name = "shop/item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["colors"] = Item.colors.all()
        return context


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
