from django import template

register = template.Library()

@register.filter(name='format_duration')
def format_duration(value):
    hours, minutes = divmod(value, 60)
    return f'{hours} hours {minutes} minutes'