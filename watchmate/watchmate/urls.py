
from django.contrib import admin
from django.urls import path, include

import watchlist_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include('watchlist_app.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]