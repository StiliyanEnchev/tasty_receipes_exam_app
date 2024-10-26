from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from common.utils import get_profile, get_receipts
from recipes.forms import RecipeCreateForm, RecipeEditForm
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
    model = Recipes
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Recipes.objects.filter(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ingredients = self.object.ingredients
        context['ingredient_list'] = ingredients.split(', ')

        return context

class RecipeEditView(UpdateView):
    template_name = 'edit-recipe.html'
    model = Recipes
    form_class = RecipeEditForm
    success_url = reverse_lazy('catalog')
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Recipes.objects.filter(pk=pk)