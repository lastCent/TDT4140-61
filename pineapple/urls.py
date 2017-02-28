"""pineapple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import quiz.views
import mainMenu.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainMenu.views.index),
    url(r'^add_question/', quiz.views.add_question),
    url(r'^base/', quiz.views.base),
    url(r'^courses/$', quiz.views.courses_page),
    url(r'^exercises/(?P<course_id>[0-9]+)/$', quiz.views.exercises_page),
    url(r'^question/(?P<exer_id>[0-9]+)/$', quiz.views.view_question),
]
