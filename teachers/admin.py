from django.contrib import admin

from .models import Teachers


@admin.register(Teachers)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age')
    list_filter = ('age', 'last_name')
    search_fields = ('last_name_startswith',)