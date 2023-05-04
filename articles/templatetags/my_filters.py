from django import template

register = template.Library()

@register.filter
def isinstance(instance, classinfo):
    return isinstance(instance, classinfo)