from rest_framework import serializers
from movies_list.models import Movie


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'actors', 'genre','release_date','rating']


class (serializers.ModelSerializer)