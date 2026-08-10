from django import forms
from .models import Training

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training

        fields = [
            'training_name',
            'training_type',
            'trainer_name',
            'trainer_email',
            'start_date',
            'end_date',
            'training_hours',
            'organiser',
            'training_status',
        ]

        widgets = {
            'start_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
            'end_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }