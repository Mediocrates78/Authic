from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title
