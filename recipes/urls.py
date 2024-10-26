from django.urls import path, include

from recipes.views import RecipeCreateView, RecipeCatalog, RecipeDetailsView, RecipeEditView

urlpatterns = [
    path('create/', RecipeCreateView.as_view(), name='create-recipe'),
    path('catalogue/', RecipeCatalog.as_view(), name='catalog'),
    path('<int:pk>/details/', RecipeDetailsView.as_view(), name='details-view'),
    path('<int:pk>/edit/', RecipeEditView.as_view(), name='edit-recipe'),
    ]
