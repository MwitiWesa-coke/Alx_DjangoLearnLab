from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Book Actions (Custom Permissions)
    path('books/add/', views.add_book, name='add_book'),
    path('add_book/', views.add_book), 

    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('edit_book/<int:pk>/', views.edit_book),

    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

    # Dashboards
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),

    # Auth
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Book List & Library Detail
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
