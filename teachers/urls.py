from django.urls import path

from teachers.views import create_teacher, list_teachers, edit_teacher, delete_teacher


urlpatterns = [
    path('create_teacher', create_teacher, name='create-teacher'),
    path('list_teachers/', list_teachers, name='list-teachers'),
    path('edit_teacher/<int:teacher_id>', edit_teacher, name='edit-teacher'),
    path('delete_teacher/<int:teacher_id>', delete_teacher, name='delete-teacher'),
]
