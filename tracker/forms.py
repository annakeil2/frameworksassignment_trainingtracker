from django import forms
from .models import Training, Staff
from .models import Message

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
        
class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        sender_id = kwargs.pop('sender_id')
        super(MessageForm, self).__init__(*args, **kwargs)
        raw_staff = Staff.objects.exclude(id=sender_id)
        staff = [(q.id, q.get_full_name()) for q in raw_staff]
        self.fields['receiver_user_id'] = forms.ChoiceField(
            choices=tuple(staff)
        )
        
    class Meta:
        model = Message

        fields = [
            'id',
            # 'sender_user_id',
            'receiver_user_id',
            'subject',
            'body',
            # 'message_status',
        ]

        widgets = {
            'body': forms.Textarea(
                attrs={'cols': 80, 'rows': 20}
            ),
        }
        
        
        
        
        
# class MessageStatusFormSet(forms.BaseModelFormSet):
#     # def __init__(self, *args, **kwargs):
#     #     selected_status_id = kwargs.pop('selected_status_id')
#     #     super(MessageForm, self).__init__(*args, **kwargs)
#     class Meta:
#         model = Training
                
#     statuses = [(key, Message.MESSAGE_STATUS[key]) for key in Message.MESSAGE_STATUS]
#     message_status = forms.ChoiceField(
#         choices=tuple(statuses)
#     )     