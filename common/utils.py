from recipes.models import Recipes
from profiles.models import Profile


def get_profile():
    return Profile.objects.first()


def get_receipts():
    return Recipes.objects.all()

def get_specific_recipt(self, pk):
    pk = self.kwargs.get('pk')
    return Recipes.objects.filter(pk=pk)