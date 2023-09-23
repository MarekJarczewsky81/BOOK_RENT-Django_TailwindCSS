from django.urls import path
from .views import book_title_list_view, book_title_detail_view

app_name = 'books'

urlpatterns = [

    path('', book_title_list_view, name='main'),
    path('<pk>/', book_title_detail_view, name='detail-book'),
]
