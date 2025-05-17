from django.db import models
from authentication.models import CustomUser
from books.models import Book

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    borrowed_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.user.role})"