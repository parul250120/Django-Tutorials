from django.urls import path, include

# from .views import movie_list, movie_details
from .views import WatchListAV, WatchListDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='streamplatform-detail')

]
