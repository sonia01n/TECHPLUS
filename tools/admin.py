from django.contrib import admin
from .models import Tool

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'category', 'is_trending', 'created_at')
    list_filter = ('category', 'is_trending')
    search_fields = ('name', 'company')
    list_editable = ('is_trending',)