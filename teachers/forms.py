from django import forms

from .models import Teachers


class TeacherForm(forms.Form):
    first_name = forms.CharField(label='Teacher\'s first name', required=True)
    last_name = forms.CharField(label='Teacher\'s last name', required=True)
    age = forms.IntegerField(label='Teacher\'s first age', required=True)
    seniority = forms.IntegerField(label='Teacher\'s seniority')


class TeachersFormFromModel(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ['first_name', 'last_name', 'age', 'seniority']
