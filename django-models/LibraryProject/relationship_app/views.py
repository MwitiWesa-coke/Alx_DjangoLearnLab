from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic.detail import DetailView  # ✅ correct class name
from .models import Book, Library

# == Role Check Functions ==
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userproflie.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.profile.role == 'Member'

# == Role-Based Views ==
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
    
#  Login view
def register(request):
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

