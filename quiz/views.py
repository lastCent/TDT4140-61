from django.shortcuts import render
from django.http import HttpResponse
from quiz.forms import TestForm


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
