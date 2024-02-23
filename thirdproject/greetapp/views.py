import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def datetimeinfo(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = '<h1>Hello guest very '
    if h < 12:
        msg += 'Good Morning!!!!'
    elif h<16:
        msg += 'Good Afternoon!!!'
    elif h<21:
        msg += 'Good Evening!!!'
    else:
        msg += 'Good Night......'
    msg += '</h1><hr>'
    msg += '<h3>server date and time is : '+str(date)+'</h3>'
    return  HttpResponse(msg)