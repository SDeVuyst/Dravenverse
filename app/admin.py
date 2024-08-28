from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin

from .models import Character, Article

@admin.register(Character)
class CharacterAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('name', 'age', 'role')
    ordering = ('id',)

    search_fields = ('name', 'age', 'role', 'backstory', 'description_short'),

@admin.register(Article)
class ArticleAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('title', 'author', 'type')
    ordering = ('-updated',)

    search_fields = ('title', 'author', 'type', 'short_intro', 'content'),
