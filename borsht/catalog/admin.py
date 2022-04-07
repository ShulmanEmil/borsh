from django.contrib import admin

# Register your models here.
from .models import Dish
from .models import Category

admin.site.register(Dish)
admin.site.register(Category)
