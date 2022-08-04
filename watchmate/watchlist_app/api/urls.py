from django.urls import path, include

# from .views import movie_list, movie_details
from rest_framework.routers import DefaultRouter

from .views import WatchListAV, WatchListDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV, ReviewList, ReviewDetail, \
    ReviewCreate, StreamPlatformVS

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchListDetailsAV.as_view(), name='watchlist-detail'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    # path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='streamplatform-detail'),

    path('', include(router.urls)),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')


]
