from rest_framework import generics 
from .serializers import MovieList ,MovieSerializer , GenreSerializer , MovieDetailSerializer,WatchListSerializer,ReviewSerializer ,CreateMovie
from .models import Movie , Genre, WatchList
from movies_list import serializers
from .serializers import UserLoginSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView


from rest_framework.permissions import  IsAuthenticated, IsAdminUser

# Create your views here.

class MovieCreate(CreateAPIView):
    serializer_class = CreateMovie
    def perform_create(self, serializer):
        serializers.save(user.self)


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieList

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Movie.objects.filter(movie_watchlist__user=self.request.user)
        else: 
            queryset = Movie.objects.all
        return queryset


class MovieCreate(generics.CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes= [IsAdminUser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WatchedListCreate(generics.CreateAPIView):
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self,serializer):
        movie_obj=Movie.objects.get(id=self.kwargs['object_id'])
        serializer.save(user=self.request.user,movie=movie_obj)
        


class GenreCreate(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes= [IsAdminUser]

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = 'object_id'


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
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)



class WatchListView(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        movie_id = self.kwargs['movie_id']
        return WatchList.objects.get(user=user, movie_id=movie_id)




class ReviewView(generics.CreateAPIView):
   serializer_class = ReviewSerializer
   permission_classes= [IsAdminUser] 


class UpdateWatchListView(generics.CreateAPIView):

    permission_classes= [IsAuthenticated,] 
    serializer_class = WatchListSerializer
   
    def perform_create(self, serializer):
        user = self.request.user 
        serializer.save(user=user)
