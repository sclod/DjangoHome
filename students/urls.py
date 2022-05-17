from django.urls import path

from students.views import get_student, list_students, create_student, edit_student, delete_student, index, manually_generate_students, email_form
urlpatterns = [
    path('', index),
    path('get_student/', get_student),
    path('list_students/', list_students, name='list-students'),
    path('edit_student/<int:student_id>', edit_student, name='edit-student'),
    path('delete_student/<int:student_id>', delete_student, name='delete-student'),
    path('create_student', create_student, name='create-student'),
    path('genereate_students_form', manually_generate_students, name='genereate-students-form'),
    path('email_form', email_form, name='email_form'),
]
