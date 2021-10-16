from django.shortcuts import render

# Create your views here.

def index(request):
 return render(request, 'book_manager/index.html')

def book_management(request):
    return render(request, 'book_manager/book_management.html')

def author_management(request):
    return render(request, 'book_manager/author_management.html')

def contact(request):
    return render(request, 'book_manager/contact.html')