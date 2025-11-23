from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import RedirectView
router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'watchlist', views.WatchlistViewSet, basename='watchlist')

urlpatterns = [
    # Make sure this says 'api/' not 'apj/'
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/movies/')),
]