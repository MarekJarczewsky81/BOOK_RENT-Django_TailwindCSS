from django.shortcuts import render
from .models import BookTitle
from django.views.generic import ListView
# Create your views here.

class BookTitleListView(ListView):
    model = BookTitle
    template_name = 'books/main.html'
    context_object_name = 'qs'
    # model_list.html -> booktitle_list.html
    # context or query set is : object_list


# def book_title_list_view(request):
#     qs = BookTitle.objects.all()
#     return render(request, 'books/main.html', {'qs': qs})


def book_title_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    obj = BookTitle.objects.get(pk=pk)
    return render(request, 'books/detail.html', {'obj': obj})
