
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # fields="__all__"
        help_texts = {
            "password2":None,
            "username":None,
        }

        fields = ('first_name', 'last_name', 'email','username',  'password1', 'password2')
        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.PasswordInput(attrs = {'class':'form-control ','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.PasswordInput(attrs = {'class':'form-control', 'type':'password', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

# class LoginForm(forms.Mod):






