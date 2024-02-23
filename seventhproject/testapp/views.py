from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
def exams_view(request):
    return HttpResponse('<h1>Exams View</h1>')
def attendance_view(request):
    return HttpResponse('<h1>Attendance View</h1>')
def fees_view(request):
    return HttpResponse('<h1>Fees View</h1>')

