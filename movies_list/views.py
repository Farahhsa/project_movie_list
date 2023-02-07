from rest_framework import generics 
from .serializers import MovieList ,MovieSerializer , GenreSerializer , MovieDetailSerializer,WatchListSerializer
from .models import Movie , Genre, WatchList
from movies_list import serializers
from .serializers import UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.permissions import  IsAuthenticated, IsAdminUser

# Create your views here.
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieList

class MovieCreate(generics.CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes= [IsAdminUser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes= [IsAdminUser]

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = "id"


class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer
 


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
<<<<<<< HEAD
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)



class WatchListView(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

=======
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
>>>>>>> e7d35a3e5c8904cef30c917eca8b6c3479ac9492
