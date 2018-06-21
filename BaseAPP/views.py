from django.shortcuts import render
from .forms import SubForms
from products.models import Product, ProductImage

# Create your views here.

def subscribers(request):
    name = "zohan" #Можем передать переменную в страницу через шаблон
    form = SubForms(request.POST or None)  #Для передачи forms в шаблоне, присваеваем переммной реквест пост
    if request.method == "POST":  #Если метод пердачи пост, сохранить форму
        SaveForm = form.save()
    return render(request, 'subscribers.html', locals()) #Без locals не отобразит в шаблоне переменную

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)  #Отфильтровуем Кверисет который у нас уже есть
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'home.html', locals())