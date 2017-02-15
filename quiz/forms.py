# coding=utf-8
""" This is where forms for the quiz module are stored """
from django import forms


class TestForm(forms.Form):
    """ Can be used get data from user """
    name = forms.CharField()
    num = forms.IntegerField()
