from tkinter import N
from re import I
from django.db import models
from students.models import Student
from teachers.models import Teachers


class Group(models.Model):
    name_group = models.CharField(max_length=50, null=True
    name_group = models.CharField(max_length=50, unique=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='students'

    def __str__(self):
        return f'{self.name_group} {self.teacher} {self.students}'
