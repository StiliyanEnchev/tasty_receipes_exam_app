from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from common.utils import get_profile, get_receipts
from recipes.forms import RecipeCreateForm
from recipes.models import Recipes


# Create your views here.
class RecipeCreateView(CreateView):
    template_name = 'create-recipe.html'
    form_class = RecipeCreateForm
    model = Recipes
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        form.instance.author = get_profile()
        return super().form_valid(form)

class RecipeCatalog(ListView):
    template_name = 'catalogue.html'
    queryset = get_receipts()



class RecipeDetailsView(DetailView):
    template_name = 'details-recipe.html'
    queryset = get_receipts()
