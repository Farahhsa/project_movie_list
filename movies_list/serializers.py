from .models import Movie, Genre
from rest_framework import serializers

class MovieList(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'actors', 'genre','release_date','rating']

class MovieSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Movie 
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre 
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name','actors','genre','release_date','rating']