from django.contrib import admin
from .models import NewsArticle

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'related_tool', 'published_date')
    list_filter = ('source', 'related_tool')
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'