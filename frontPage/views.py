from django.shortcuts import render
from frontPage.forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

#Spartansk placeholder
def index(request):
    if request.method=='POST':
        if 'login-submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request,'add_question.html')  # Redirect etter innlogging
            else:
                return render(request, 'index.html')        # Redirect etter feilet innlogging
        elif 'register-submit' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid() and request.POST['password'] == request.POST['confirm-password']:
                group = Group.objects.get(name='Student')
                stud = User.objects.create_user(
                    username=request.POST['username'],
                    email=request.POST['email'],
                    password=request.POST['password'])
                stud.groups.add(group)
                return render(request, 'base.html') # Redirect etter registrering
            else:
                return render(request, 'index.html') # Redirect etter feilet registrering

    else:
        return render(request, 'index.html')