# Create
>>> from bookshelf.models import Book
>>> b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> b
# <Book: 1984 by George Orwell>

# Retrieve
>>> from bookshelf.models import Book
>>> Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell>]>

# Update
>>> b = Book.objects.get(title="1984")
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
>>> b
# <Book: Nineteen Eighty-Four by George Orwell>

# Delete
>>> b = Book.objects.get(title="Nineteen Eighty-Four")
>>> b.delete()
# (1, {'bookshelf.Book': 1})
>>> Book.objects.all()
# <QuerySet []>
