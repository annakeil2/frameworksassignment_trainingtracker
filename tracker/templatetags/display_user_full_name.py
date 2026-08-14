from django import template
from tracker.models import Staff

register = template.Library()

@register.filter    
def display_user_full_name(user_id):
    user = Staff.objects.get(pk=user_id)
    print('display_user_full_name', user_id, user)
    full_name = user.get_full_name()
    if full_name: 
        return full_name
    return user.username
