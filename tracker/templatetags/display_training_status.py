from django import template
from tracker.models import Training

register = template.Library()

@register.filter    
def display_training_status(status):
    return Training.TRAINING_STATUS[status]