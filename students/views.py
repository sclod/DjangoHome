from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm, StudentFormFromModel
from .models import Student


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
