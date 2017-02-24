from django.shortcuts import render
from django.http import HttpResponse
from quiz.forms import QuestionForm
from quiz.models import Question


def add_question(request):
    """ Loads template to get neccecary data for the question object, and saves it to database """
    added = False
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()     # uncertain part
            added = True
            form = QuestionForm()
    else:
        form = QuestionForm()

    q_list = Question.objects.all()
    return render(request, 'add_question.html', {'form': form, 'added': added, 'questions': q_list})


def view_question(request):
    """ Displayes the question in the answer-question site """
    if request.method == 'POST':
        pass
    else:
        que = Question.objects.get(id=1)
        context = {
            'question': que.question,
            'alt_1': que.alternative_1,
            'alt_2': que.alternative_2,
            'alt_3': que.alternative_3,
            'alt_4': que.alternative_4,
        }
        return render(request, 'view_question.html', context)


def base(request):
    return render(request, 'base.html')

