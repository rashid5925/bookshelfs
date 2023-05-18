from django.db import models
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=5000)
    def __str__(self):
        return self.name
    
class Quote(models.Model):
    book_title = models.CharField(max_length=500)
    quote = models.CharField(max_length=2000)
    def __str__(self):
        return self.book_title
    
class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=255)
    rating = models.FloatField()
    no_of_rating = models.IntegerField()
    image = models.FileField()
    file = models.FileField()

class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
