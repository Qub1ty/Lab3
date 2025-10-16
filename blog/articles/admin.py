# articles/admin.py
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'text', 'author__username')
    readonly_fields = ('created_date',)
    ordering = ('-created_date',)

    def get_excerpt(self, obj):
        return obj.get_excerpt()
    get_excerpt.short_description = "Превью"
