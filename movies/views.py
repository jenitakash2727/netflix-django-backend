from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Movie, Genre, Watchlist
from .serializers import MovieSerializer, GenreSerializer, WatchlistSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get'])
    def trending(self, request):
        trending_movies = Movie.objects.order_by('-rating')[:10]
        serializer = self.get_serializer(trending_movies, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.GET.get('q', '')
        movies = Movie.objects.filter(title__icontains=query)
        serializer = self.get_serializer(movies, many=True)
        return Response(serializer.data)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.AllowAny]


class WatchlistViewSet(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)