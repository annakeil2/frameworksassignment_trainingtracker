from django import template
from tracker.models import Training

register = template.Library()

@register.filter    
def display_training_type(type):
    """Convert a training type in to its string"""
    return Training.TRAINING_TYPE[type]