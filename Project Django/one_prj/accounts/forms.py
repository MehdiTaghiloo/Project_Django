from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


class UserRegisterationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        models = User
        fields = '__all__'
    
    


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
