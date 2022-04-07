from django.shortcuts import redirect
from .models import Profile
from django.views import generic
from .models import Favorites
from django.contrib.auth.models import User
from catalog.models import Dish

class ProfilelView(generic.DetailView):
    model = Profile


class FavotitesView(generic.ListView):

    model = Favorites

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(FavotitesView, self).get_context_data(**kwargs)
        print(context['favorites_list'])
        return context




class AddFavoritesView(generic.View):
    def post(self, request, *args, **kwargs):
        dish_id = int(request.POST.get('dish_id'))
        user_id = int(request.POST.get('user_id'))
        url_from = request.POST.get('url_from')

        user_inst = User.objects.get(id=user_id)
        dish_inst = Dish.objects.get(id=dish_id)

        try:
            dish_favorite_inst = Favorites.objects.get(dish=dish_inst, user=user_inst)
        except Exception as e:
            print(dish_inst, user_inst)
            dish_favorite = Favorites(user=user_inst, dish=dish_inst, favorite=True)
            dish_favorite.save()

        return redirect(url_from)


class RemoveFavoritesView(generic.View):
    def post(self, request, *args, **kwargs):
        dish_favorite_id = int(request.POST.get('dish_favorite_id'))
        url_from = request.POST.get('url_from')

        dish_favorite = Favorites.objects.get(id=dish_favorite_id)
        dish_favorite.delete()

        return redirect(url_from)
