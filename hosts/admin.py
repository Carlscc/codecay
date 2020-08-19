from django.contrib import admin

from .models import Host

class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')


admin.site.register(Host, HostAdmin)
