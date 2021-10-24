from django.contrib import admin
from .models import Author, Genre, Book, SupportTicket

# Register your models here.
admin.site.register(Genre)
admin.site.register(SupportTicket)

class AuthorBooks(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    inlines = [AuthorBooks]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    list_filter = ('genre',)




