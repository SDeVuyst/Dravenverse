from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from unfold.admin import ModelAdmin

from .models import Character

@admin.register(Character)
class SponsorAdmin(SimpleHistoryAdmin, ModelAdmin):
    list_display = ('name', 'age', 'role')
    ordering = ('id',)

    search_fields = ('name', 'age', 'role', 'backstory', 'description_short'),
