from django.contrib import admin
from .models import Category, Attraction, Event

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class AttractionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'time', 'attraction', 'created_at')
    search_fields = ('name', 'attraction__name')
    list_filter = ('date', 'attraction')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Attraction, AttractionAdmin)
admin.site.register(Event, EventAdmin)