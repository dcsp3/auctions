from django.contrib import admin

from .models import Listings, Comments, Watchlist

# Register your models here.

admin.site.register(Listings)
admin.site.register(Comments)
admin.site.register(Watchlist)
