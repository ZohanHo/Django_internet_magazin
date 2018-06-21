from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, DetailView, ListView


from products.models import Product

# Create your views here.

class MyView(View):

    def get(self, *args, **kwargs): #Вызывается метод dispatch, который определяет с каким методом запрос к нам пришел (GET или Post), вызыает функцию
        return HttpResponse ("Привет, мир")



class MyTemplateView(TemplateView):
    template_name = 'one/one.html'

    def get_context_data(self, **kwargs):
        context = super(MyTemplateView, self).get_context_data(**kwargs)
        context['name'] = Product.objects.all()[:4]
        return context


class MyDetailView(DetailView):  #Используя класс можем отрисовывать поля, по pk, которыу указали в регулярке urls
    model = Product
    template_name = 'one/one.html'

def ShowTime(request):
    zohan = 61
    name = Product.objects.filter(name__icontains=123)
    return render (request, 'one/one.html', {"Tantum": id}, locals())

class MyListView(ListView):
    model = Product
    template_name = 'one/one.html'

    def dispatch(self, request, *args, **kwargs):
        self.zohan = request.GET.get('Grom')
        return super(MyListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Product.objects.all().order_by(self.zohan)[:2]
