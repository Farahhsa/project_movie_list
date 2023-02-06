from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()

# Create your models here.
class Genre(models.Model):
    Movie = models.ForeignKey()

class Movie(models.Model):
     name = models.CharField(max_length=100)
     actors = models.TextField
     genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
     release_date = models.DateField()
     rating = models.FloatField(default=0)


class WatchList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField()

class Reting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])











    
