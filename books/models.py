from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    available = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.title