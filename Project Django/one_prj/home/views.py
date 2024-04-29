from django.shortcuts import render
from accounts.forms import UserLoginForm

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def main_page(request):
    return render(request, 'main.html')
