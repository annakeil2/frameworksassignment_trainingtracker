from django import forms
from .models import Training, Employee
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
        raw_staff = Employee.objects.exclude(id=sender_id)
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
       
        
class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        
    class Meta:
        model = Employee

        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        
    class Meta:
        model = Employee

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit: 
            user.save()
        return user