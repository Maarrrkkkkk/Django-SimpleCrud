from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from book.views import book_list, book_new, book_detail, book_edit, book_delete, book_restore, deleted_books
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='home'),
    path('books/', book_list, name='book_list'),
    path('book/new/', book_new, name='book_new'),
    path('book/<slug:slug>/', book_detail, name='book_detail'),
    path('book/<slug:slug>/edit/', book_edit, name='book_edit'),
    path('book/<slug:slug>/delete/', book_delete, name='book_delete'),
    path('book/<slug:slug>/restore/', book_restore, name='book_restore'),
    path('deleted_books/', deleted_books, name='deleted_books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)