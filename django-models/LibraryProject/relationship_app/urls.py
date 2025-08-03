from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.user_register, name='register'),

    # Book list view
    path('books/', views.list_books, name='book-list'),

    # Library detail view (expects pk in URL)
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]
