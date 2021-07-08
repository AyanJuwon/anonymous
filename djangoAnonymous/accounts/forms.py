from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Confirm password'}))
                   


    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        help_texts = {
            'username': None,
            'password1':None,
            'password2':None
        }

 