from django.db import models
from products.models import Product
from django.db.models.signals import post_save

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "Статус {}".format(self.name)

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказа"

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #Общая цена для всех товаров в заказе
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=24, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=48, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)


    def __str__(self):
        return "Заказ {} {}".format(self.id, self.status.name)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1) #Количество
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0) #Цена
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #Общая цена = Цена * количество
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.product.name)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def save(self, *args, **kwargs):  #Переопределение метода save
        price_per_item = self.product.price    #Говорим что цена = тукущей цене
        self.price_per_item = price_per_item # Говорим что цену которую взяли сейчас равно цене
        self.total_price = self.nmb * price_per_item #Цена всего = цена * на количество
        super(ProductInOrder, self).save(*args, **kwargs)



def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductInOrder)

class ProductInBasket(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1) #Количество
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0) #Цена
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #Общая цена = Цена * количество
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.product.name)

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    def save(self, *args, **kwargs):  #Переопределение метода save
        price_per_item = self.product.price    #Говорим что цена = тукущей цене
        self.price_per_item = price_per_item # Говорим что цену которую взяли сейчас равно цене
        self.total_price = int(self.nmb) * price_per_item #Цена всего = цена * на количество
        super(ProductInBasket, self).save(*args, **kwargs)