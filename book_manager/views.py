from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView, UpdateView
from .models import Book, Author
from book_manager.forms import CreateBook



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

class UpdateBook(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book_manager/updatebook.html'

class SearchResultsView(ListView):
    model = Book
    template_name = 'book_manager/searchresults.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(title__icontains=query)
        return object_list

def create_book(request):
    form = CreateBook(request.POST or None)
    if form.is_valid():
        form.save()

        messages.success(request, 'The book as been added.')
        return redirect('create-book')
    context = {
        'form': form
    }
    
    return render(request, 'book_manager/createbook.html', context=context)

def search_book(request):
    pass

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