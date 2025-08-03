>>> b = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> b
# <Book: Nineteen Eighty-Four by George Orwell>
