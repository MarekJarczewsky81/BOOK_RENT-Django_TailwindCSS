from django.shortcuts import render
from .models import BookTitle
# Create your views here.


def book_title_list_view(request):
    qs = BookTitle.objects.all()
    return render(request, 'books/main.html', {'qs':qs})