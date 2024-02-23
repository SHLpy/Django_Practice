from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')

