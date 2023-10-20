from django import forms
from .models import BookTitle

class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('title', 'publisher', 'author')