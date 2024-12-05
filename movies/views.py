from django.shortcuts import render, redirect
from .models import Movie, Actor

def movie_list(request):
    sort_by = request.GET.get('sort_by', 'title')  # Default sort by title
    movies = Movie.objects.all().order_by(sort_by)
    for movie in movies:
        movie.actor_count = movie.actor_count()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def actor_list(request):
    actors = Actor.objects.all()
    for actor in actors:
        actor.movie_count = actor.movie_count()
    return render(request, 'movies/actor_list.html', {'actors': actors})

def vote_movie(request, movie_id, action):
    movie = Movie.objects.get(id=movie_id)
    if action == "upvote":
        movie.upvotes += 1
    elif action == "downvote":
        movie.downvotes += 1
    movie.save()
    return redirect('movie_list')

def upvote_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.upvotes += 1
    movie.save()
    return redirect('movie_list')

def downvote_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.downvotes += 1
    movie.save()
    return redirect('movie_list')
