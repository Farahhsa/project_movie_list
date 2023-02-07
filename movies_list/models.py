from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator


User = get_user_model()

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre
    
class Movie(models.Model):
     name = models.CharField(max_length=100)
     actors = models.TextField()
     genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movie')
     release_date = models.DateField()
     user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='movie')

     def __str__(self):
        return self.name

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watchlist')
    watched = models.BooleanField()



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()

class Reting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])











    
