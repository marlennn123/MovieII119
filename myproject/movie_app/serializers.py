from .models import (UserProfile, Country, Director,
                     Actor, Genre, Movie, MovieLanguages,
                     Moments, Rating, Favorite, FavoriteMovie,
                     History)
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%Y')
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_image', 'movie_name', 'year',
                  'country', 'genre','status_movie']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Rating
        fields = ['id', 'user', 'parent', 'stars', 'text', 'created_date']


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format('%d-%m-%Y'))
    country = CountrySerializer(many=True)
    director = DirectorSerializer(many=True)
    actor = ActorSerializer(many=True)
    genre = GenreSerializer(many=True)
    movie_frames = MomentsSerializer(many=True, read_only=True)
    movie_videos = MovieLanguagesSerializer(many=True, read_only=True)
    movie_ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country', 'director', 'actor', 'genre',
                  'types', 'movie_time', 'movie_image', 'movie_trailer', 'description',
                  'status_movie', 'movie_frames', 'movie_videos', 'movie_ratings']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


