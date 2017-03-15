from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.

def studentPage(request):
    page = loader.get_template('studentPage.html')
    return HttpResponse(page.render())