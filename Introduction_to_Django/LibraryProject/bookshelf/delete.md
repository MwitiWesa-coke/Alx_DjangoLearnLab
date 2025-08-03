>>> b = Book.objects.get(title="Nineteen Eighty-Four")
>>> b.delete()
# (1, {'bookshelf.Book': 1})
>>> Book.objects.all()
# <QuerySet []>
