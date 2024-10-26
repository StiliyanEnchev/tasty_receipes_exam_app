from django.core.validators import MinLengthValidator
from django.db import models

from profiles.validators import first_letter_upper_validator


# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(
        unique=True,
        max_length=20,
        validators=[
            MinLengthValidator(
                limit_value=2,
                message="Nickname must be at least 2 chars long!"
        )])

    first_name = models.CharField(
        max_length=30,
        validators=[first_letter_upper_validator]
    )

    last_name = models.CharField(
        max_length=30,
        validators=[first_letter_upper_validator]
    )

    chef = models.BooleanField(
        default=False
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

