# from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    value = 'hello world 5'
    return render(request, 'main.html', {'key_in_the_template': value})
