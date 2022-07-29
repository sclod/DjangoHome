from django.urls import reverse_lazy

from .models import Teachers

from django.views.generic import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ListTeacherView(ListView):
    model = Teachers
    template_name = 'teacher/teacher_list.html'


class TeacherCreateView(CreateView):
    model = Teachers
    template_name = 'teacher/teacher_form.html'
    fields = ['first_name', 'last_name', 'age']
    success_url = reverse_lazy('list-teachers')


class TeacherUpdateView(UpdateView):
    model = Teachers
    template_name = 'teacher/edit_teacher_form.html'
    fields = ['first_name', 'last_name', 'age']
    success_url = reverse_lazy('list-teachers')

class TeacherDeleteView(DeleteView):
    model = Teachers
    template_name = 'teacher/teacher_confirm_delete.html'
    success_url = reverse_lazy('list-teachers')
