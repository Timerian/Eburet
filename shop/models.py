from colorfield.fields import ColorField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator


# Available colors of items
class Color(models.Model):
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    color = ColorField(default='000000')

    def __str__(self):
        return self.color


# Categories of furniture
class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=50, verbose_name="Название категории")

    def __str__(self):
        return f'{self.name}'


# Model of furniture
class Item(models.Model):
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    name = models.CharField(max_length=30, verbose_name="Название предмета")
    vendor_name = models.CharField(max_length=20, verbose_name="Артикул", default="-", null=True)
    price = models.IntegerField(verbose_name="Стоимость в рублях")
    description = models.TextField(max_length=500, verbose_name="Описание")
    concept = models.CharField(max_length=100, verbose_name="Концепт", blank=True, null=True)
    material = models.TextField(max_length=300, verbose_name="Материал")
    equipment = models.TextField(max_length=500, verbose_name="Комплектация")
    peculiarities = models.TextField(max_length=500, verbose_name="Особенности")
    guarantee = models.TextField(max_length=500, verbose_name="Гарантийный срок")
    parameters = models.TextField(max_length=300, default=None, verbose_name="Параметры")
    production_time = models.CharField(max_length=150, verbose_name="Время изготовления", blank=True)

    categories = models.ManyToManyField(Category, related_name="categories", verbose_name="Категории")

    def __str__(self):
        return f"{self.name}"


# Model of order
class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    INDIVIDUAL = 'IND'
    ENTITY = 'ENT'
    PAYMENT_METHODS = [
        (INDIVIDUAL, 'Car payment for individual'),
        (ENTITY, 'Cashless payment for entity')
    ]

    first_name = models.CharField(max_length=100, verbose_name="Имя")
    second_name = models.CharField(max_length=100, verbose_name="Фамилия")
    email = models.EmailField(verbose_name="Адрес электронной почты")
    phone_number = PhoneNumberField(null=False, unique=True, verbose_name="Номер телефона")
    address = models.TextField(max_length=500, verbose_name="Адрес")
    comment = models.TextField(max_length=500, verbose_name="Комментарии к заказу")
    promo_code = models.CharField(max_length=12, verbose_name="Промокод")
    pay_method = models.CharField(max_length=3, choices=PAYMENT_METHODS, default=INDIVIDUAL, verbose_name="Метод оплаты")
    agreement = models.BooleanField(default=False, verbose_name="Согласие на обработку персональных данных")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оформления заказа")
    complete = models.BooleanField(default=False, null=True, blank=True, verbose_name="Выполнен")

    def __str__(self):
        return f"{self.first_name} {self.second_name} | {self.created_date}"


# model of available colors for each item and its quantity
class ItemColor(models.Model):
    class Meta:
        verbose_name = "Цвет предмета"
        verbose_name_plural = "Цвета предметов"

    quantity = models.IntegerField(default=0)

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Предмет")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name="Цвет предмета")

    def __str__(self):
        return f"{self.item.name} | {self.color} | {self.quantity}"


# model of item in order including its quantity
class OrderItem(models.Model):
    class Meta:
        verbose_name = "Предмет из заказа"
        verbose_name_plural = "Предметы из заказов"

    item = models.ForeignKey(ItemColor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Предмет")
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Заказ")
    quantity = models.IntegerField(default=0, blank=True, null=True, verbose_name="Количество предметов в заказе")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")

    def __str__(self):
        return f"{self.item} |{self.quantity} | {self.order}"


# function for creating the path to the directory where image of the item will be stored ("media/*item_name*/")
def file_directory_path(instance, filename):
    return f"{instance.item.name}/{filename}"


# model of image for the item
class ImageItem(models.Model):
    class Meta:
        verbose_name = "Изображение предмета"
        verbose_name_plural = "Изображения предметов"

    image = models.FileField(verbose_name="Изображение", upload_to=file_directory_path)

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Предмет")

    def __str__(self):
        return f"{self.item.name} | {self.image.name}"
