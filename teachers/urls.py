from django.urls import path

from teachers.views import create_teacher, list_teachers, edit_teacher, delete_teacher


urlpatterns = [
    path('create_teacher', create_teacher),
    path('list_teachers/', list_teachers, name='list-teacher'),
    path('edit_teacher/<int:teacher_id>', edit_teacher),
    path('delete_teacher/<int:teacher_id>', delete_teacher, name='delete-teacher'),
]
