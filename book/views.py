from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm
from django.db import IntegrityError
import requests 
from bs4 import BeautifulSoup


def book_list(request):
    active_books = Book.objects.filter(is_deleted=False)
    deleted_books = Book.objects.filter(is_deleted=True)

    return render(request, 'books/book_list.html', {
        'active_books': active_books,
        'deleted_books': deleted_books,
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    try:
        cover_image_url = book.cover_image.url
    except ValueError:
        cover_image_url = 'default_cover_image.jpg' 
    return render(request, 'books/book_detail.html', {'book': book, 'cover_image_url': cover_image_url})

def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                book = form.save()
                return redirect('book_list')
            except IntegrityError:
                form.add_error(None, 'A book with this title or slug already exists.')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


def book_edit(request, slug):
    # Get the book from the database
    book = get_object_or_404(Book, slug=slug)

    if request.method == "POST":
        # The form is being submitted
        # Create a form instance and populate it with data from the request
        form = BookForm(request.POST, instance=book)

        # Check if the form is valid
        if form.is_valid():
            # Save the form data but don't commit to the database yet
            book = form.save(commit=False)

            # Update the cover image URL
            cover_image_url = request.POST.get('cover_image')  # Changed 'cover_image_url' to 'cover_image'
            if cover_image_url:
                book.cover_image = cover_image_url  # Changed 'book.cover_image_url' to 'book.cover_image'

            # Save the book to the database
            book.save()

            # Redirect to the list of books
            return HttpResponseRedirect('/books/')
    else:
        form = BookForm(instance=book)

    
    return render(request, 'books/book_edit.html', {'form': form})
def book_delete(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book.delete()
    return HttpResponseRedirect('/books/')

def book_restore(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book.restore()
    return HttpResponseRedirect('/books/')

def deleted_books(request):
    deleted_books = Book.objects.filter(is_deleted=True)
    return render(request, 'deleted_books.html', {'deleted_books': deleted_books})

def get_book_cover(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_cover_div = soup.find('div', {'class': 'bc-box-inner'})
    book_cover_img = book_cover_div.find('img')
    return book_cover_img['src']


