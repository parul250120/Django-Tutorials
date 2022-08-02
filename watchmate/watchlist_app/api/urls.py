from django.urls import path, include

# from .views import movie_list, movie_details
from .views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailsAV.as_view(), name='movie-details'),

]
