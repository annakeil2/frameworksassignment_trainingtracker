from django.shortcuts import render, redirect

from .models import Training
from django.conf import settings


def training_self(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_trainings = Training.objects.filter(id=user_id)
        context = {"user_id": user_id, "trainings": user_trainings}
        return render(request, "training/training_self.html", context)
    else:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    
def training_user(request, user_id):
    if request.user.is_authenticated:
        
        a_list = Training.objects.filter(id=user_id)
        # context = {"year": year, "article_list": a_list}
        return render(request, "training/training_self.html")
    else:
        return redirect('login_url')