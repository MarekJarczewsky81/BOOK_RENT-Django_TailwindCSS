# from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import Book, BookTitle


def home_view(request):
    qs = Customer.objects.all()
    # obj = Book.objects.get(id=1)
    obj = BookTitle.objects.get(id=1)
    books = obj.books
    title = obj.title
    print(books)
    print(title)
    context = {
        'qs': qs,
        'obj': obj
    }
    return render(request, 'main.html', context)
