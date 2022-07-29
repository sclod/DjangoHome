from django.urls import path

from students.views import (
    get_student,
    manually_generate_students,
    email_form,
    index,
    ListStudentView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)
urlpatterns = [
    path('', index.as_view()),
    path('student/', ListStudentView.as_view(), name='list-students'),

    path('student/add/', StudentCreateView.as_view(), name='create-student'),
    path('student/<int:pk>/', StudentUpdateView.as_view(), name='edit-student'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='delete-student'),

    path('genereate_students_form', manually_generate_students, name='genereate-students-form'),
    path('email_form', email_form, name='email_form'),
    path('get_student/', get_student),
]
