from django.shortcuts import render
from django.http import HttpResponse
from .models import Group
from .forms import GroupForm


def create_group(request):
    if request.method == 'GET':
        form = GroupForm()
    elif request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            Group.objects.create(**form.cleaned_data)
            return HttpResponse('Group created')
    return render(request, 'group.html', {'form': form})
