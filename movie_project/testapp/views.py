from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'testapp/index.html')

from testapp.models import Movie
def list_movies_view(request):
    movie_list = Movie.objects.all()
    return render(request,'testapp/listmovies.html',{'movie_list':movie_list})

