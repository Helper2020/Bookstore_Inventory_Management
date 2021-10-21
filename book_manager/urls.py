from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('book_management/', views.book_management, name='book-management'),
     path('book_management/search-results', views.SearchResultsView.as_view(), name='search-results'),
     path('book_management/create-book', views.create_book, name='create-book'),
     path('book_management/update-book/<int:pk>', views.UpdateBook.as_view(), name='update-book'),
     path('book_catalog/', views.BookCatalog.as_view(), name='book-catalog'),
     path('book_catalog/<int:pk>', views.BookInfo.as_view(), name='book-info'),
     path('author_management/', views.author_management, name='author-management'),
     path('author_catalog/', views.AuthorCatalog.as_view(), name='author-catalog'),
     path('author_catalog/<int:pk>', views.AuthorInfo.as_view(), name='author-info'),
     path('contact/', views.contact, name='contact'),
]