from django.urls import path

from teachers.views import (
    ListTeacherView,
    TeacherCreateView,
    TeacherUpdateView,
    TeacherDeleteView,
)

urlpatterns = [
    path('teacher/', ListTeacherView.as_view(), name='list-teachers'),
    path('teacher/add/', TeacherCreateView.as_view(), name='create-teacher'),
    path('teacher/<int:pk>/', TeacherUpdateView.as_view(), name='edit-teacher'),
    path('teacher/<int:pk>/delete/', TeacherDeleteView.as_view(), name='delete-teacher'),
]
