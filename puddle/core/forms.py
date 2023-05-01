from django.forms import forms
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import  User
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {
            'placeholder': 'Введите логин',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    
    password = forms.CharField(widget = forms.PasswordInput(attrs = {
            'placeholder': 'Введите пароль',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))


class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

        username = forms.CharField(widget = forms.TextInput(attrs = {
            'placeholder': 'Введите логин',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        email = forms.CharField(widget = forms.EmailInput(attrs = {
            'placeholder': 'Введите почту',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        password1 = forms.CharField(widget = forms.PasswordInput(attrs = {
            'placeholder': 'Введите пароль',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        password2 = forms.CharField(widget = forms.PasswordInput(attrs = {
            'placeholder': 'Повторитере пароль',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))