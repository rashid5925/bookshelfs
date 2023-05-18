from django.contrib import admin
from .models import Contact, Quote, Book, Favourite

class ContactAdmin(admin.ModelAdmin):
    list_display= ('name', 'email', 'subject', 'message')

class QuoteAdmin(admin.ModelAdmin):
    list_display= ('book_title', 'quote')

class BookAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'rating', 'no_of_rating', 'image', 'file')

class FavouritesAdmin(admin.ModelAdmin):
    list_display= ('user', 'book')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Favourite, FavouritesAdmin)

