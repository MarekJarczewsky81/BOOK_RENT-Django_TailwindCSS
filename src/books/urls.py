from django.urls import path
from .views import book_title_list_view

app_name = 'books'

urlpatterns = [

    path('', book_title_list_view),

]
