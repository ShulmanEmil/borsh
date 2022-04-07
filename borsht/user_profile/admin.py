from django.contrib import admin

# Register your models here.
from .models import Profile
from .models import Favorites

admin.site.register(Profile)
admin.site.register(Favorites)
