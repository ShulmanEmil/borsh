from django.urls import path, include
from . import views
from django.urls import re_path as url

from .views import AddFavoritesView, RemoveFavoritesView


app_name = 'favorite'

urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.ProfilelView.as_view(), name='profile-detail'),
    path('favorites/', views.FavotitesView.as_view(), name='favorites'),
    path('favorite/', include([
        path('add/', AddFavoritesView.as_view(), name='add'),
        path('remove/', RemoveFavoritesView.as_view(), name='remove')
    ])),
]
