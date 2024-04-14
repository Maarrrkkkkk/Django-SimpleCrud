from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    cover_image = forms.URLField()
    

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'publication_date', 'number_of_pages', 'cover_image']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'