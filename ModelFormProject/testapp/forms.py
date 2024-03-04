from django import forms
from testapp.models import Student
class StudentForm(forms.ModelForm):
    name = forms.CharField()
    marks = forms.IntegerField()
    class Meta:
        model = Student
        fields = '__all__'
