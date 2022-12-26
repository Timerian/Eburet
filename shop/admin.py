from django.contrib import admin
from .models import Item, Order, OrderItem, Color, Category, ItemColor, ImageItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "email", "phone_number", "created_date")
    ordering = ("created_date", )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("item", "order", "quantity", "date_added")


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemColor)
class ItemColorAdmin(admin.ModelAdmin):
    list_display = ("item", "color", "quantity")


@admin.register(ImageItem)
class ImageItem(admin.ModelAdmin):
    list_display = ("item", "image")
    sortable_by = ("item", )


