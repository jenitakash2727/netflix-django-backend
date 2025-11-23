from rest_framework import serializers
from .models import Movie, Genre, Watchlist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class WatchlistSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Watchlist
        fields = '__all__'