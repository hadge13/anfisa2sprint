from django.shortcuts import render
#from django.db.models import Q
from ice_cream.models import Category, IceCream

def index(request):
    template = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.values('id', 'title', 'price', 'description'
        ).filter(is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True)  # Категория разрешена к публикации.
    
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
        #'categories': categories
    }
    return render(request, template, context)

#ice_cream_list = IceCream.objects.values('title','description').filter(
        #(Q(is_on_main=True) & Q(is_published = True))
        #| (Q(title__contains='пломбир') & Q(is_published=True))

#categories = Category.objects.values('id', 'output_order', 'title').order_by(
        # Сортируем записи по значению поля output_order,
        # а если значения output_order у каких-то записей равны -
        # сортируем эти записи по названию в алфавитном порядке.
        #'output_order', 'title' )

#ice_cream_list = IceCream.objects.values('title','id','description').filter(
        #Q(is_on_main=True)
        #).order_by('title')[1:4]  
