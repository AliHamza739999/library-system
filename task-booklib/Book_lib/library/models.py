from django.db import models

# Create your models here.
class Author(models.Model):
    frist_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.frist_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length = 256, unique=True)
    author = models.ForeignKey(Author , on_delete = models.CASCADE , blank = False , null = False)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=100)
    price = models.DecimalField(max_digits= 50 , decimal_places = 3 )
    
    def __str__(self):
        return f"{self.title} {self.author}"
