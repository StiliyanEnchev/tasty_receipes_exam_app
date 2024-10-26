from django import forms

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

