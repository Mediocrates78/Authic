from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_input_field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input_field'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form_input_field'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form_input_field'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input_field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input_field'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

