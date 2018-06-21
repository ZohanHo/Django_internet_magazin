from django.contrib import admin
from .models import Product, ProductImage, ProductCategory

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage  #используем для работы модель картинок
    extra = 0 #Количество отображенных полей для картинок, при необходимости можно добавить с админки

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory,ProductCategoryAdmin)

class ProductAdmin (admin.ModelAdmin):   #Добавляет поля в админке, в разные колонки

    list_display = [field.name for field in Product._meta.fields]  #Выводит все поля какие есть
    inlines = [ProductImageInline] #Для товара админки использовать класс наследованный от табуляринлайнс дает возможность добавить, удалить картинку

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):   #Добавляет поля в админке, в разные колонки

    list_display = [field.name for field in ProductImage._meta.fields]  #Выводит все поля какие есть

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)