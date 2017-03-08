# coding=utf-8
""" This is where forms for the frontPage module are stored """
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password')
