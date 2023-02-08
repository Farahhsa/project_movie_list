from .models import Movie, Genre, WatchList,Review
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class MovieList(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'actors', 'genre','release_date']

class WatchListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    watched = serializers.BooleanField(read_only=True)
    class Meta:
        model = WatchList
        fields = ['user', 'movie','watched']

class MovieSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
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
        fields = ['id','name','actors','genre','release_date']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
        ]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user =  User(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()

        return user



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    access = serializers.CharField(allow_blank=True, read_only=True)

       

    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")

        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist")

        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination!")

        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)

        data["access"] = token
        return data

class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = ['user','movie','review','rating']
