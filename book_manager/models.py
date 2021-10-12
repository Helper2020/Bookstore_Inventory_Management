from django.db import models
from django.urls import reverse 

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre')

    def get_absolute_url(self):
        return reverse('genre-info', args=[str(self.id)])

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Birth', null=True, blank=True)
    date_of_death = models.DateField('Death', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-info', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    synopsis = models.TextField(max_length=1000, help_text='A summary of the book content.')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13-digit ISBN')
    price = models.DecimalField('Price', max_digits=3, decimal_places=2)
    quantity = models.IntegerField('Quantity', help_text='Quanity in stock.')
    genre = models.ForeignKey(Genre, help_text='Select genre.' , on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('book-info', args=[str(self.id)])

    def __str__(self):
        return self.title
    

 

