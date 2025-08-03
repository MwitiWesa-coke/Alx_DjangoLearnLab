from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic.detail import DetailView  # ✅ correct class name
from .models import Book, Library

# 🔐 Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # or use reverse() for named URLs
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# 🔓 Logout view
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# 📝 Register view
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # assumes you've named this URL
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# 📚 Function-based view to list books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 🏛️ Class-based view for library detail
class LibraryDetailView(DetailView):  # ✅ fixed typo: was "Detailview"
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

