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
from django.contrib.auth import views as auth_views
import quiz.views
import frontPage.views
import courses.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', frontPage.views.login_view),
    url(r'^add_question/', quiz.views.add_question),
    url(r'^base/', quiz.views.base),
    url(r'^courses/$', quiz.views.courses_page),
    url(r'^course/(?P<course_id>[\w\-]+)/$', quiz.views.exercises_page),
    url(r'^question/(?P<exer_id>[0-9]+)/$', quiz.views.view_question),
    url(r'^view_question/', quiz.views.view_question),
    url(r'^base/', quiz.views.base),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password_change/$', auth_views.password_change, name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_change/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^courses/', courses.views.courses),
    url(r'^test/$', quiz.views.test)
    ]