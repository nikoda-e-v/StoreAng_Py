from django.contrib import admin
from .models import Seller, Customer, Category, Product, Order, Cart, Stock # Импортируем модели из models.



# Register your models here.
## Создаем классы для админ-панели
# Продавец
class SellerAdmin(admin.ModelAdmin):
  pass
admin.site.register(Seller, SellerAdmin)

# Покупатель
class CustomerAdmin(admin.ModelAdmin):
  pass
admin.site.register(Customer, CustomerAdmin)

# Категория
class CategoryAdmin(admin.ModelAdmin):
  pass
admin.site.register(Category, CategoryAdmin)

# Продукт
class ProductAdmin(admin.ModelAdmin):
  pass
admin.site.register(Product, ProductAdmin)

# Заказ
class OrderAdmin(admin.ModelAdmin):
  pass
admin.site.register(Order, OrderAdmin)

# Корзина
class CartAdmin(admin.ModelAdmin):
  pass
admin.site.register(Cart, OrderAdmin)

# Склад
class StockAdmin(admin.ModelAdmin):
  pass
admin.site.register(Stock, OrderAdmin)