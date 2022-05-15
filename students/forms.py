from django import forms

from .models import Student


class StudentForm(forms.Form):
    first_name = forms.CharField(label='Student\'s first name', required=True)
    last_name = forms.CharField(label='Student\'s last name', required=True)
    age = forms.IntegerField(label='Student\'s first age', required=True)
    phone = forms.CharField(label='Student\'s phone', required=True)


class StudentFormFromModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age']
