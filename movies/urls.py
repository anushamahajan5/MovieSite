from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('actors/', views.actor_list, name='actor_list'),
    path('vote/<int:movie_id>/<str:action>/', views.vote_movie, name='vote_movie'),
    path('upvote/<int:id>/', views.upvote_movie, name='upvote_movie'),
    path('downvote/<int:id>/', views.downvote_movie, name='downvote_movie'),
]
