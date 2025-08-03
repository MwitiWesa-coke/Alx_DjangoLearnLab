>>> b = Book.objects.get(title="1984")
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
>>> b
# <Book: Nineteen Eighty-Four by George Orwell>
