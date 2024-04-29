from django.shortcuts import render, redirect
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.

# registration view
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid(): # check the inputs are valid
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.save()
            messages.success(request, 'Your registred successfully.', 'success')
            return redirect('home')
    else:
        form = UserRegisterationForm(request.POST)
        
    return render(request, 'register.html', {'form' : form})

# login view
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully.', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Your username or password is wrong!', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})

# logout view
def user_logout(request):
    logout(request)
    messages.success(request, 'logged out!', 'danger')
    return redirect('main')
            
