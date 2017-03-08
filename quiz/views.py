from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from quiz.forms import QuestionForm
from quiz.models import Question, Course, CourseExercises, Exercise, CourseMembers


@permission_required('lecturer')
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


def base(request):
    return render(request, 'base.html')


@login_required
def view_question(request, exer_id):
    """ Displayes the question in the answer-question site """
    # todo: må finne ut hvilken bruker som er logget inn
    if request.method == 'POST':
        pass
    else:
        exercise = Exercise.objects.get(id=exer_id)
        que = None    # todo: fjern de som allerede er i results
        context = {
            'question': que.question,
            'alt_1': que.alternative_1,
            'alt_2': que.alternative_2,
            'alt_3': que.alternative_3,
            'alt_4': que.alternative_4,
        }
        return render(request, 'view_question.html', context)


@login_required
def exercises_page(request, course_id):
    current_user = User(request.user)
    if current_user.has_perm('student'):
        course_exercises = CourseExercises.objects.filter(course=course_id)
        exercises = [ce.exercise for ce in course_exercises]
        return render(request, 'exercises.html', {'exercises': exercises})
    elif current_user.has_perm('lecturer'):
        pass
    else:
        pass


@login_required
def courses_page(request):
    """get's CourseMember matchin the logged in persons pk. Then retrievs the Courses from the CourseMember objects"""
    current_user = request.user
    course_member = CourseMembers.objects.filter(student=current_user.id)
    courses = [cm.course for cm in course_member]
    return render(request, 'courses.html', {'courses': courses})
