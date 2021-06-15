from django.contrib import admin
from django.contrib import Seller


# Register your models here.
## Импортируем модель User(по умолчанию) из фреймфорка Джанго.
class SellerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Seller, SellerAdmin)