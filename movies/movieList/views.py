from django.shortcuts import render, redirect
from movieList.models import movie
from movieList.forms import movieCreation

def listView(request):
    # List all the movies
    all_movies = movie.objects.all()
    return render(request, 'movieList/index.html',{'all_movies':all_movies})

def addMovies(request):
    # View for adding movies
    movie_add = movieCreation()
    if request.method == 'POST':
        movie_add=movieCreation(request.POST)
        if movie_add.is_valid():
            movie_add.save()
            return redirect('list')
    return render(request,'movieList/addmovie.html',{'movie_add':movie_add})