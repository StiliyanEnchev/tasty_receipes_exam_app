from django import forms

from common.mixins import ReadOnlyMixin
from recipes.models import Recipes


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipes
        exclude = ['author']
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'Optional image URL here...'}),
            'instructions': forms.Textarea(attrs={'placeholder': 'Enter detailed instructions here...'}),
            'ingredients': forms.Textarea(attrs={'placeholder': "ingredient1, ingredient2, ..."}),
        }


class RecipeEditForm(RecipeCreateForm):
    pass

class DeleteRecipeForm(ReadOnlyMixin, RecipeCreateForm):
    read_only_fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']
