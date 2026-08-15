from django import template
from tracker.models import Training

register = template.Library()

@register.filter    
def display_training_status(status):
    """Convert a training status int to its string"""
    return Training.TRAINING_STATUS[status]