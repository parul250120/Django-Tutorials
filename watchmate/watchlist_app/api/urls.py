from django.urls import path, include

# from .views import movie_list, movie_details
from rest_framework.routers import DefaultRouter

from .views import WatchListAV, WatchListDetailsAV, StreamPlatformAV, StreamPlatformDetailsAV, ReviewList, ReviewDetail, \
    ReviewCreate, StreamPlatformVS, UserReview, WatchListGV

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchListDetailsAV.as_view(), name='watchlist-detail'),
    path('list2/', WatchListGV.as_view(), name='watchlist-test'),
    # path('reviews/<str:username>/', UserReview.as_view(), name='user-reviews'),
    path('reviews/', UserReview.as_view(), name='user-reviews'),

    # path('stream/', StreamPlatformAV.as_view(), name='stream-platform'),
    # path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(), name='streamplatform-detail'),

    path('', include(router.urls)),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail')

]
