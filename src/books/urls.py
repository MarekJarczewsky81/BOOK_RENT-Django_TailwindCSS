from django.urls import path
from .views import BookTitleListView, book_title_detail_view

app_name = 'books'

urlpatterns = [

    path('', BookTitleListView.as_view(), name='main'),
    path('<pk>/', book_title_detail_view, name='detail-book'),
]
