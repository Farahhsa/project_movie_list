from django.shortcuts import render
from rest_framework.generics import ListAPIView
from movies_list.models import Movie
from .serializers import ListSerializer

# Create your views here.

class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = ListSerializer



 




