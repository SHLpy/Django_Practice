from django.shortcuts import render

# Create your views here.
def display(request):
    return render(request,'testapp/results.html')

