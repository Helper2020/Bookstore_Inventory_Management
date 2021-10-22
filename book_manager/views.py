from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.views.generic import ListView, UpdateView
from .models import Book, Author
from book_manager.forms import CreateAuthor, CreateBook



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

class UpdateAuthor(UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'book_manager/updateauthor.html'

class SearchBooksResultsView(ListView):
    model = Book
    template_name = 'book_manager/searchbookresults.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(title__icontains=query)
        return object_list

class SearchAuthorResultsView(ListView):
    model = Author
    template_name = 'book_manager/searchauthorresults.html'
    
    def get_queryset(self):
        first_name = self.request.GET.get('firstname')
        last_name = self.request.GET.get('lastname')
        object_list = Author.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name)
        return object_list

def create_author(request):
    
    form = CreateAuthor(request.POST or None)
    if form.is_valid():
        form.save()

        messages.success(request, 'The author has been added.')
        return redirect('create-author')

    context = {
        'form': form
    }

    return render(request, 'book_manager/createauthor.html', context=context)

def create_book(request):
    form = CreateBook(request.POST or None)
    if form.is_valid():
        form.save()

        messages.success(request, 'The book has been added.')
        return redirect('create-book')
    context = {
        'form': form
    }
    
    return render(request, 'book_manager/createbook.html', context=context)
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