from django.contrib import admin
from .models import Subscribers

class SubscriberAdmin(admin.ModelAdmin):   #Добавляет поля в админке, в разные колонки
    #list_display = ['name', 'email', 'id'] #Выводим конкретные поля
    list_display = [field.name for field in Subscribers._meta.fields]  #Выводит все поля какие есть
    #fields = ["email"]   #Поля которые необходимо включить, можно указать все через запятую
    #exclude = ["id"]   #Поля которые необходимо исключить, если не указать, покажет все
    list_filter = ['name',] #Добавить фильтр по полю, отображаеется в админке справа
    search_fields = ['name'] #Поиск по определеному полю в админке

    class Meta:
        model = Subscribers

admin.site.register(Subscribers, SubscriberAdmin)


