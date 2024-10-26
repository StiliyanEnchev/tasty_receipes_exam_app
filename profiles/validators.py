from django.core.exceptions import ValidationError


def first_letter_upper_validator(value):
    if value[0] != value[0].upper():
        raise ValidationError(
            'Name must start with a capital letter!'
        )

