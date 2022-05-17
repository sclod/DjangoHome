from tkinter import E
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import GenerateRandomStudentForm, StudentForm, StudentFormFromModel, MessageEmail
from .models import Student
from .tasks import create_random_students, email_send


def index(request):
    return render(request, 'index.html')


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



def list_students(request):
    students_list = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students_list})


def create_student(request):
    if request.method == 'GET':
        form = StudentForm()
    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            Student.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse('list-students'))
    return render(request, 'student/create_student_form.html', {'form': form})


def edit_student(request, student_id):
    if request.method == 'POST':
        form = StudentFormFromModel(request.POST)
        if form.is_valid():
            Student.objects.update_or_create(defaults=form.cleaned_data, id=student_id)
            return HttpResponseRedirect(reverse('list-students'))
    elif request.method == 'GET':
        student = Student.objects.filter(id=student_id).first()
        form = StudentFormFromModel(instance=student)
    return render(request, 'student/edit_student_form.html', {'form': form, 'student_id': student_id})


def delete_student(request, student_id):
        student = Student.objects.filter(id=student_id)
        student.delete()
        return HttpResponseRedirect(reverse('list-students'))
