from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def actor_count(self):
        return MovieActorRelation.objects.filter(movie=self).count()

class Actor(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    def movie_count(self):
        return MovieActorRelation.objects.filter(actor=self).count()

class MovieActorRelation(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

