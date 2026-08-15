from django import template
from tracker.models import Training

register = template.Library()

@register.simple_tag    
def selected_option(value, default):
    print('selected_option', value, default)
    if value == default:
        return "selected='selected'"
    else: 
        return ""