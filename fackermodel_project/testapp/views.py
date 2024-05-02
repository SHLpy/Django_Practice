from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def Student_view(request):
    students = Student.objects.all
    return render(request, 'testapp/StudentData.html', {'students' : students})