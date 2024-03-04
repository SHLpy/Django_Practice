from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.

def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Record inserted into database successfully....')
    form = StudentForm()
    return render(request,'testapp/studentform.html',{'form':form})
