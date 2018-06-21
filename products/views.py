from django.shortcuts import render
from products.models import *
# Create your views here.

def product(request, product_id):          # Принимает название переменной которую мы указали в url
    product = Product.objects.get(id=product_id)  # Вытягивает через кверисет гет из продакnf через id

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'products/product.html', locals())

#td2qzrxjq61htr0xdntdzzyoz8xc6gyh
