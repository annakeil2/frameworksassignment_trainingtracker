from django.shortcuts import render, redirect

from .models import Training, Message
from django.conf import settings
from .forms import TrainingForm, MessageForm
from . import services

def training_self(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_trainings = Training.objects.filter(user_id=user_id)
        total = services.get_total_number_of_trainings(user_trainings)
        ongoing_training = services.get_number_of_ongoing_trainings(user_trainings)
        completed_training = services.get_number_of_completed_trainings(user_trainings)
        context = {
            "user_id": user_id,
            "trainings": user_trainings,
            "total_training": total,
            "ongoing_training": ongoing_training,
            "completed_training": completed_training
        }
        return render(request, "training/training_list.html", context)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
    
def training_user(request, user_id):
    # To-do: Remember to check the user is in HR #
    if request.user.is_authenticated:
        user_trainings = Training.objects.filter(id=user_id)
        context = {"user_id": user_id, "trainings": user_trainings}
        return render(request, "training/training_list.html", context)
    else:
        return redirect('login_url')
    
    
# def training_form(request):
#     return render(request, "training/training_form.html")

def inbox(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        messages = Message.objects.filter(receiver_user_id=user_id)
        # status_form =  MessageStatusForm(initial={'message_status': })
        context={
            "messages": messages
        }
        return render(request, "messages/inbox.html", context)
    else:
        return redirect('login_url')

def outbox(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        messages = Message.objects.filter(sender_user_id=user_id)
        context={
            "messages": messages
        }
        return render(request, "messages/outbox.html", context)
    else:
        return redirect('login_url')
    
def message_detail(request, message_id):
    print('message_id', message_id)
    if request.user.is_authenticated:
        message = Message.objects.get(id=message_id)
        context={
            "message": message
        }
        return render(request, "messages/message_detail.html", context)
    else:
        return redirect('login_url')


def compose(request):
        
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == 'POST':
            form = MessageForm(request.POST, sender_id=user_id)
    
            if form.is_valid():
                message = form.save(commit=False)
                print(message, user_id)
                message.sender_user_id = request.user.id
                message.message_status = Message.ACTIVE
                message.save()
                return redirect('inbox')
        
        else:
            form = MessageForm(sender_id=user_id)
        
        return render(
            request,
            'messages/compose.html',
            {'form': form}
        )
    else:
        return redirect('login_url')

def training_form(request):
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TrainingForm(request.POST)
    
            if form.is_valid():
                training = form.save(commit=False)
                training.user_id = request.user.id
                training.save()
                return redirect('training_self')
        
        else:
            form = TrainingForm()
        
        return render(
            request,
            'training/training_form.html',
            {'form': form}
        )
    else:
        return redirect('login_url')