from django.urls import path
from . import views
from django.urls import re_path as url


urlpatterns = [
    path('', views.DishListView.as_view(), name='index'),
    url(r'^(?P<category_slug>[-\w]+)/$',
    views.dish_list,
    name='dish_list_by_category'),
]
