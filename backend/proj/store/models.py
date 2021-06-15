from django.db import models

# Create your models here.
## Импортируем модель User(по умолчанию) из фреймфорка Джанго.
from django.contrib.auth.models import User

## Создаем класс Seller (Продавец).
class Seller(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default='0')

## Создаем класс Customer (Покупатель).
class Customer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    address = models.TextField(default='')
    geo_location = models.CharField(max_length=250, default='')

## Создаем класс Category (Категория товара).
class Category(models.Model):
    name = models.CharField(max_length=250, default='')

## Создаем класс Product (Товар).
class Product (models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product', null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True) #При удалении - не удаляются записи в связанных таблицах


## Создаем класс Stock (Склад).
class Stock(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE, null=True, blank=True) #При удалении - удаляются все записи в таблице Product
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True) #При удалении - удаляются все записи в таблице Product
    price = models.DecimalField(max_digits=10, decimal_places=2)



## Создаем класс Order (Заказ).
class Order(models.Model):
    STATUS = (
            ('new', 'new order'),
            ('pending', 'new pending'),
            ('finished', 'new finished')
        ) #Переменная для передачи статуса заказа (кортеж кортежей)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True, blank=True)#При удалении - удаляются все записи в таблице Customer
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, default='new', choices=STATUS)

## Создаем класс Cart (Заказ).
class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True, blank=True)#При удалении - удаляются все записи в таблице Product
    order = models.ForeignKey(Order,on_delete=models.CASCADE, null=True, blank=True)#При удалении - удаляются все записи в таблице Order
    ammount = models.IntegerField(default=0)
