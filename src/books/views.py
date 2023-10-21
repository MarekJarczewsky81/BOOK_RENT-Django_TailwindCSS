from django.shortcuts import render
from .models import BookTitle
from django.views.generic import ListView, FormView
from .forms import BookTitleForm
from django.urls import reverse, reverse_lazy
# Create your views here.

class BookTitleListView(FormView, ListView):
    # model = BookTitle
    queryset = BookTitle.objects.all() # [:3] # it is limiting the choosen object to 3
    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm
    # success_url = reverse_lazy('books:main')
    # model_list.html -> booktitle_list.html
    # context or query set is : object_list
    # ordering = ('-created',)

    def get_success_url(self):
        return self.request.path
    
    def get_queryset(self):
        parameter = 's'
        return BookTitle.objects.filter(title__startswith=parameter)
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        return super().form_invalid(form)
        
    
        
    
# def book_title_list_view(request):
#     qs = BookTitle.objects.all()
#     return render(request, 'books/main.html', {'qs': qs})


def book_title_detail_view(request, **kwargs):
    pk = kwargs.get('pk')
    obj = BookTitle.objects.get(pk=pk)
    return render(request, 'books/detail.html', {'obj': obj})
