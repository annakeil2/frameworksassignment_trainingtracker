import os
from tracker.models import Employee
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not Employee.objects.filter(username='anna').exists():
            Employee.objects.create_superuser(
                username='anna',
                password=os.environ.get('SU_PASSWORD')
            )
            print('Superuser has been created.')
        else:
            print('Superuser already exists.')