from rest_framework import generics 
from rest_framework.generics import ListAPIView
from .serializers import MovieList ,MovieSerializer , GenreSerializer , MovieDetailSerializer
from .models import Movie , Genre

# Create your views here.

class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieList

class MovieCreate(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "movie_id"
 




