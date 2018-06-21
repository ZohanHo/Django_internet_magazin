from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Категория товар"
        verbose_name_plural = "Категория товаров"

class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    discount = models.IntegerField(default=0) #Для поля Интегерфилд достаточно указать что default=0
    category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discription = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Тоаров"



class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='productimage') #related_name прописан для обратной связи queryset
    image = models.ImageField(blank=True, upload_to='media/products_images')  #Upload - куда будут сохранятся файлы
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"