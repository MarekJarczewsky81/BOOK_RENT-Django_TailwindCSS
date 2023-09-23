from django.shortcuts import render
from .models import BookTitle
# Create your views here.


def book_title_list_view(request):
    qs = BookTitle.objects.all()
    return render(request, 'books/main.html', {'qs': qs})


def book_title_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    obj = BookTitle.objects.get(pk=pk)
    return render(request, 'books/detail.html', {'obj': obj})
