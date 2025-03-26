from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField('Author', related_name='books', blank=True)

    def __str__(self):
        return f"Book {self.id}: {self.name}"

    def __repr__(self):
        return f"<Book {self.id}>"

    @staticmethod
    def get_by_id(book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(book_id):
        book = Book.get_by_id(book_id)
        if book:
            book.delete()
            return True
        return False

    @staticmethod
    def create(name, description, count=10, authors=None):
        book = Book(name=name, description=description, count=count)
        book.save()
        if authors:
            book.authors.set(authors)
        return book

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [author.id for author in self.authors.all()],
        }

    def update(self, name=None, description=None, count=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if count is not None:
            self.count = count
        self.save()

    def add_authors(self, authors):
        self.authors.add(*authors)
        self.save()

    def remove_authors(self, authors):
        self.authors.remove(*authors)
        self.save()

    @staticmethod
    def get_all():
        return Book.objects.all()

class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}: {self.book.name} by {self.user.username}"