from django.contrib import admin
from .models import ReadBook, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class ReadBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'quote1', 'consideration1', 'quote2', 'consideration2',
                    'quote3', 'consideration3', 'consideration4', 'user')
    list_display_links = ('id', 'title', 'user')


admin.site.register(Category, CategoryAdmin)
admin.site.register(ReadBook, ReadBookAdmin)

