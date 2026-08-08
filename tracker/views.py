from django.shortcuts import render, redirect

from .models import Training


def training_self(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        a_list = Training.objects.filter(id=user_id)
        # context = {"year": year, "article_list": a_list}
        return render(request, "training/training_self.html")
    else:
        return redirect('login_url')
    
def training_user(request, user_id):
    if request.user.is_authenticated:
        
        a_list = Training.objects.filter(id=user_id)
        # context = {"year": year, "article_list": a_list}
        return render(request, "training/training_self.html")
    else:
        return redirect('login_url')