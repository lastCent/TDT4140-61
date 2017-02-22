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
        que = Question.objects.get(id=1)    # todo: prob. not working
        cd = que.clean()
        context = {
            'question': cd['question'],
            'alt_1': cd['alt_1'],
            'alt_2': cd['alt_2'],
            'alt_3': cd['alt_3'],
            'alt_4': cd['alt_4'],
        }
        return render(request, 'view_question.html', context)

