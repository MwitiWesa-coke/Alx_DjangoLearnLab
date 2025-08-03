from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Initialize the router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: Keep BookList endpoint (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # DRF router handles all CRUD URLs for BookViewSet
    path('', include(router.urls)),
]
