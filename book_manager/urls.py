from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('book_management', views.book_management, name='book_management'),
     path('author_management', views.author_management, name='author_management'),
     path('contact', views.contact, name='contact'),
]