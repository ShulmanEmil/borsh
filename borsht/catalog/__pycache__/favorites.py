from django import temlate

from apps.user_profile.models import favorites

register = template.library()

@register.simple_tag(takes_context=True)
def is_favorite(context, dish_id):
    try:
        dish_favorite = Favorites.objects.get(dish=dish_id, user=request.user.id).favorite
    except Exception as e:
        favorite = False
    return favorite


@register.simple_tag()
def dish_favorite_id(context, dish_id):
    request = context('request')
    return Favorites.objects.get(dish=dish_id, user=request.user.id).id
