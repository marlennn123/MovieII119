from .views import (UserProfileViewSet, CountryViewSet,
                    DirectorViewSet, ActorViewSet,
                    GenreViewSet, MovieListAPIView, MovieDetailAPIView,
                    MovieLanguagesViewSet, MomentsViewSet,
                    RatingViewSet, FavoriteViewSet,
                    FavoriteMovieViewSet, HistoryViewSet)
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'country', CountryViewSet)
router.register(r'director', DirectorViewSet)
router.register(r'actor', ActorViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'movie_lan', MovieLanguagesViewSet)
router.register(r'moments', MomentsViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_item', FavoriteMovieViewSet)
router.register(r'history', HistoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail')
]