# coding=utf-8
""" This is where forms for the quiz module are stored """
from django import forms
from quiz.models import Question


class TestForm(forms.Form):
    """ Can be used get data from user """
    name = forms.CharField()
    num = forms.IntegerField()


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
