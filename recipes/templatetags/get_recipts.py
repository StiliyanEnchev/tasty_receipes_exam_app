from django import template

from common.utils import get_receipts

register = template.Library()

@register.simple_tag
def get_receipts_for_user():
    return get_receipts()