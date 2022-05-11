from django import forms

from .models import Group


class GroupForm(forms.Form):
    name_group = forms.CharField(label='Groups name', required=True)


class GroupFormFromModel(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name_group']
