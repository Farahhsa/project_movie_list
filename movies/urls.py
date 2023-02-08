"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies_list.views import MovieListView , MovieCreate , GenreCreate , MovieDetail, WatchListView
from movies_list.views import RegisterView, WatchListView,UpdateWatchListView , WatchedListCreate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from movies_list.views import UserLoginAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/movies/add/', MovieCreate.as_view(), name = 'add_moviews'),
    path('api/movies_list/', MovieListView.as_view(), name='movies_list'),
    path('api/movies/<int:object_id>/',MovieDetail.as_view(), name='movie_detail'), 
    path('api/genres/add/', GenreCreate.as_view(),name='add_genres'),
    path('api/register/',RegisterView.as_view(),name='api_register'),
    path('api/login/',UserLoginAPIView.as_view(),name='api_login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/watch_list/', WatchListView.as_view(), name='watch_list'),
    path('api/watch_list/<int:object_id>/', WatchedListCreate.as_view(), name='WatchedListCreate'),
    path('api/updatewatchlist/', UpdateWatchListView.as_view(), name='updatewatchlist'),
    ]
