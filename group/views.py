from .models import Group

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic import ListView


class ListGroupView(ListView):
    model = Group
    template_name = 'group/group_list.html'


class GroupCreateView(CreateView):
    model = Group
    template_name = 'group/group_form.html'
    fields = ['name_group']
    success_url = reverse_lazy('list-group')