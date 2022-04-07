from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Dish, Category

# Create your views here.

class DishListView(generic.ListView):
    model = Dish


    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(DishListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def dish_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    dishs = Dish.objects.all()
    if category_slug:
        category = get_object_or_404(Category, title=category_slug)
        dishs = dishs.filter(category=category)
    return render(request,
                  'catalog/category_list.html',
                  {'category': category,
                   'categories': categories,
                   'dishs': dishs})
