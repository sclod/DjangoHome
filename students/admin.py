from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age', 'phone')
    list_filter = ('age', 'last_name', 'phone')
    search_fields = ('last_name_startswith',)
