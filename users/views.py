from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def sign_up(req):
    if req.method != "POST":
        form = UserCreationForm() 

    else: 
        form = UserCreationForm(data=req.POST)

        if form.is_valid():
            new_user = form.save()

            login(req, new_user)
            return redirect('home')

    context = {'form': form }
    return render(req, 'registration/sign_up.html', context)