from django.shortcuts import render

# Create your views here.

from testapp.forms import StudentForm

def studentinput_view(request):
    submitted = False
    sname = ''

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print('Form validation success and print data')
            print('Name:', form.cleaned_data['name'])
            print('Marks:', form.cleaned_data['marks'])
            sname = form.cleaned_data['name']
            submitted = True
    else:
        form = StudentForm()

    return render(request, 'testapp/input.html', {'form': form, 'sname': sname, 'submitted': submitted})

