from recipes.models import Recipes
from profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_cars():
    return Recipes.objects.all()