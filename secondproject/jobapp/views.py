from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobsinfo(request):
    s = '<h1>Hyderabad Jobs Information......</h1>'
    return HttpResponse(s)
def punejobsinfo(request):
    s = '<h1>Pune Jobs Information......</h1>'
    return HttpResponse(s)
def bngjobsinfo(request):
    s = '<h1>Bangalore Jobs Information......</h1>'
    return HttpResponse(s)
def biharjobsinfo(request):
    s = '<h1>BiharJobs Information......</h1>'
    return HttpResponse(s)
