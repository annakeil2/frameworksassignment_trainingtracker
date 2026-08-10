from django.shortcuts import render, redirect

from .models import Training
from django.conf import settings
from .forms import TrainingForm


def training_self(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_trainings = Training.objects.filter(user_id=user_id)
        print(user_id, user_trainings)
        context = {"user_id": user_id, "trainings": user_trainings}
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
    return render(request, "messages/inbox.html")


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