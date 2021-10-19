from django.shortcuts import render
from .models import Book, Author
from django.views import generic

# Create your views here.


class BookCatalog(generic.ListView):
    model = Book
    context_object_name = 'book_catalog'
    template_name = 'book_manager/bookcatalog.html'

    def get_queryset(self):
        return Book.objects.order_by('title')

class BookInfo(generic.DetailView):
    model = Book
    template_name = 'book_manager/bookinfo.html'
    
class AuthorCatalog(generic.ListView):
    model = Author
    context_object_name = 'author_catalog'
    template_name = 'book_manager/authorcatalog.html'
    
    def get_queryset(self):
        return Author.objects.order_by('last_name')

class AuthorInfo(generic.DetailView):
    model = Author
    template_name = 'book_manager/authorinfo.html'

def index(request):
    num_books = Book.objects.all().count()
    num_authors =  Author.objects.all().count()

    info = {
        'num_books': num_books,
        'num_authors': num_authors
    }
    
    return render(request, 'book_manager/index.html', context=info)

def book_management(request):
    return render(request, 'book_manager/book_management.html')

def author_management(request):
    return render(request, 'book_manager/author_management.html')

def contact(request):
    return render(request, 'book_manager/contact.html')