from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('book_management/', views.book_management, name='book-management'),
     path('book_catalog/', views.BookCatalog.as_view(), name='book-catalog'),
     path('book_catalog/<int:pk>', views.BookInfo.as_view(), name='book-info'),
     path('author_management/', views.author_management, name='author-management'),
     path('author_catalog/', views.AuthorCatalog.as_view(), name='author-catalog'),
     path('author_catalog/<int:pk>', views.AuthorInfo.as_view(), name='author-info'),
     path('contact/', views.contact, name='contact'),
]