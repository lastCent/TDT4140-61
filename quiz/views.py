from django.shortcuts import render
from django.http import HttpResponse
from quiz.forms import TestForm, QuestionForm
from quiz.models import Question


def test(request):
    """ this is where the back-end logic is """
    if request.method == 'POST':
        print('ok')
        form = TestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # Data in a nice format
            name = cd['name']
            number = cd['num']
            return render(request, 'test_ok.html', {'name': name, 'nice_number': number})
    else:
        form = TestForm()
        print('nope')
    return render(request, 'test_ext.html', {'form': form})

def add_question(request):
    """ Loads template to get neccecary data for the question object, and saves it to database """
    added = False
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()     # uncertain part
            added = True
            form = QuestionForm()
            # todo: test saving to models
    else:
        form = QuestionForm()

    q_list = Question.objects.all()
    return render(request, 'add_question.html', {'form': form, 'added': added, 'questions': q_list})
