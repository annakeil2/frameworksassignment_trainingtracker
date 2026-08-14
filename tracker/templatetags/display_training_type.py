from django import template
from tracker.models import Training

register = template.Library()

@register.filter    
def display_training_type(type):
    return Training.TRAINING_TYPE[type]