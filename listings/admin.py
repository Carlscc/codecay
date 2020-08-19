from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'host')
    list_display_links = ('id', 'title')
    list_filter = ('host',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'county', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
