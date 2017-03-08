from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def courses(request):
    page = loader.get_template('courses.html')
    return HttpResponse(page.render())