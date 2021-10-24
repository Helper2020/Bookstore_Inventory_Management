from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('book_management/', views.book_management, name='book-management'),
     path('book_management/search-results', views.SearchBooksResultsView.as_view(), name='book-results'),
     path('book_management/create-book', views.create_book, name='create-book'),
     path('book_management/update-book/<int:pk>', views.UpdateBook.as_view(), name='update-book'),
     path('book_catalog/', views.BookCatalog.as_view(), name='book-catalog'),
     path('book_catalog/<int:pk>', views.BookInfo.as_view(), name='book-info'),
     path('author_management/', views.author_management, name='author-management'),
     path('author_management/create-author', views.create_author, name='create-author'),
     path('author_management/author-results', views.SearchAuthorResultsView.as_view(), name='author-results'),
     path('author_management/update-author/<int:pk>', views.UpdateAuthor.as_view(), name='update-author'),
     path('author_catalog/', views.AuthorCatalog.as_view(), name='author-catalog'),
     path('author_catalog/<int:pk>', views.AuthorInfo.as_view(), name='author-info'),
     path('contact/', views.contact, name='contact')
]