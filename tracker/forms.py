from django import forms
from .models import Training, Employee
from .models import Message

class TrainingForm(forms.ModelForm):
    """A form for creating and updating training records."""
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
    """A form for creating messages"""
    def __init__(self, *args, **kwargs):
        """Initialise the form and exclude the sender from the recipient list."""
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
    """A form for viewing and updating employee details."""
    def __init__(self, *args, **kwargs):
        """Initialise the form and exclude the sender from the recipient list."""
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
    """A form for registering a new employee account."""
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        """Initialise the form and make the email field required."""
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
        """Create the employee and securely hash their password."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit: 
            user.save()
        return user