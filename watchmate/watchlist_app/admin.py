from django.contrib import admin

# Register your models here.
from watchlist_app.models import WatchList, StreamPlatform

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
