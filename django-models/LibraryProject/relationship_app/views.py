from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# Create your views here.
def list_books(request):
    books = Book.objectives.all()
    return render(request, 'list_books.html', {'books': books})

#Class-based view
class LibraryDetailView(Detailview):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
