from django.db import models

class Book(models.Model):
    name = models.CharField(blank=True, max_length=128)
    description = models.CharField(blank=True, max_length=256)
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField('author.Author', related_name='books', blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

    def __repr__(self):
        return f"Book(id={self.id})"

    @staticmethod
    def get_by_id(book_id):
        return Book.objects.get(id=book_id) if Book.objects.filter(id=book_id).exists() else None

    @staticmethod
    def delete_by_id(book_id):
        book = Book.get_by_id(book_id)
        if book:
            book.delete()
            return True
        return False

    @staticmethod
    def create(name, description, count=10, authors=None):
        if len(name) > 128:
            return None
        book = Book(name=name, description=description, count=count)
        book.save()
        if authors:
            book.authors.add(*authors)
        return book

    def update(self, name=None, description=None, count=None):
        if name: self.name = name
        if description: self.description = description
        if count is not None: self.count = count
        self.save()

    def add_authors(self, authors):
        if authors:
            self.authors.add(*authors)

    def remove_authors(self, authors):
        if authors:
            self.authors.remove(*authors)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [a.to_dict() for a in self.authors.all()]
        }

    @staticmethod
    def get_all():
        return list(Book.objects.all())
