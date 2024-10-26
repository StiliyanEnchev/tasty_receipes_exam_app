from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from recipes.choices import CuisineTypeChoices


# Create your models here.
class Recipes(models.Model):
    title = models.CharField(
        unique=True,
        max_length=100,
        validators=[MinLengthValidator(2)],
        error_messages={
            'unique': "We already have a recipe with the same title!"
        })

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineTypeChoices
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        help_text="Provide the cooking time in minutes.",
        validators=[MinValueValidator(1)]
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='recipes'
    )