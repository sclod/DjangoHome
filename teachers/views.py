from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Teachers
from .forms import TeacherForm, TeachersFormFromModel


def list_teachers(request):
    teachers_list = Teachers.objects.all()
    return render(request, 'teacher/teachers_list.html', {'teachers': teachers_list})


def create_teacher(request):
    if request.method == 'GET':
        form = TeacherForm()
    elif request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teachers.objects.create(**form.cleaned_data)
            return HttpResponse('Teacher created')
    return render(request, 'teacher/create_teacher.html', {'form': form})


def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        form = TeachersFormFromModel(request.POST)
        if form.is_valid():
            Teachers.objects.update_or_create(defaults=form.cleaned_data, id=teacher_id)
            return HttpResponseRedirect(reverse('list-teachers'))
    else:
        student = Teachers.objects.filter(id=teacher_id).first()
        form = TeachersFormFromModel(instance=student)

    return render(request, 'teacher/edit_teacher.html', {'form': form}, {'teacher_id': teacher_id})


def delete_teacher(request, teacher_id):
    teacher = Teachers.objects.filter(id=teacher_id)
    teacher.delete()
    return HttpResponseRedirect(reverse('list-teacher'))
