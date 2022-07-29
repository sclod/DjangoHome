from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import GenerateRandomStudentForm, MessageEmail, StudentForm
from .models import Student
from .tasks import create_random_students, email_send


class index(TemplateView):

    template_name = "index.html"


class ListStudentView(ListView):
    model = Student
    template_name = 'student/student_list.html'


class StudentCreateView(CreateView):
    form_class = StudentForm
    initial = {'key': 'value'}
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('list-students')
    allow_empty = False

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-students'))

        return render(request, self.template_name, {'form': form})


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/edit_student_form.html'
    fields = ['first_name', 'last_name', 'age']
    success_url = reverse_lazy('list-students')
    allow_empty = False


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('list-students')
    allow_empty = False


def get_student(request):
    if request.method == 'GET':
        name_filter = request.GET.get('first_name', '')
        students_list = Student.objects.filter(first_name=name_filter).all()
        output = '\n '.join(
            [f'{student.first_name} {student.last_name}, {student.age};' for student in students_list]
        )
        return HttpResponse(output)
    return HttpResponse('Method not found')


def manually_generate_students(request):
    if request.method == 'POST':
        form = GenerateRandomStudentForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data.get('total')
            create_random_students.delay(total)
            messages.success(request, 'We are genereate your random students!')
            return redirect('list-students')
    else:
        form = GenerateRandomStudentForm()
    
    return render(request, 'student/student_generator.html', {'form': form})


def email_form(request):
    if request.method == 'POST':
        form = MessageEmail(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            email_send.delay(title, message, email)
            messages.success(request, 'Send!')
            return redirect('list-students')
    else:
        form = MessageEmail()
    
    return render(request, 'student/email.html', {'form': form})
