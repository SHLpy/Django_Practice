from django.shortcuts import render
import datetime

# Create your views here.

# def wish(request):
#     date=datetime.datetime.now
#     my_dict={'insert_date':date}
#     return render(request,'testapp/wish.html',context=my_dict)

def wish(request):
    date = datetime.datetime.now()
    name = 'Sohail Ahmed'
    rollno = '0111Me191166'
    marks = '81.5%'
    branch ='Information Technology'
    my_dict = {'insert_date':date,'name':name,'rollno':rollno,'marks':marks,'branch':branch }
    return render(request,'testapp/wish.html',context=my_dict)
