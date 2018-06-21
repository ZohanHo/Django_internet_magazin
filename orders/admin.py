from django.contrib import admin
from .models import Status, Order, ProductInOrder, ProductInBasket

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder  #используем для работы модель картинок
    extra = 0 #Количество отображенных полей для картинок, при необходимости можно добавить с админки



class OrderAdmin(admin.ModelAdmin):   #Добавляет поля в админке, в разные колонки
    #list_display = ['name', 'email', 'id'] #Выводим конкретные поля
    list_display = [field.name for field in Order._meta.fields]  #Выводит все поля какие есть
    #fields = ["email"]   #Поля которые необходимо включить, можно указать все через запятую
    #exclude = ["id"]   #Поля которые необходимо исключить, если не указать, покажет все
    #list_filter = ['name',] #Добавить фильтр по полю, отображаеется в админке справа
    #search_fields = ['name'] #Поиск по определеному полю в админке
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)


class StatusAdmin (admin.ModelAdmin):   #Добавляет поля в админке, в разные колонки

    list_display = [field.name for field in Status._meta.fields]  #Выводит все поля какие есть

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class ProductInBasketAdmin (admin.ModelAdmin):   #Добавляет поля в админке, в разные колонки
    list_display = [field.name for field in ProductInBasket._meta.fields]  #Выводит все поля какие есть

    class Meta:
        model = ProductInBasket

admin.site.register( ProductInBasket, ProductInBasketAdmin)