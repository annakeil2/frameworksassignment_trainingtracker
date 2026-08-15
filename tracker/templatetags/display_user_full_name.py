from django import template
from tracker.models import Employee

register = template.Library()

@register.filter    
def display_user_full_name(user_id):
    """Get the fullname for an Employee from their user id"""
    user = Employee.objects.get(pk=user_id)
    full_name = user.get_full_name()
    if full_name: 
        return full_name
    return user.username
