from django import template
from decouple import config

register = template.Library()


@register.simple_tag
def get_env_var(key):
    return config(key)