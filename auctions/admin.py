from django.contrib import admin

from .models import Listings, Bid, Comments, Watchlist, Category

# Register your models here.

admin.site.register(Listings)
admin.site.register(Bid)
admin.site.register(Comments)
admin.site.register(Watchlist)
admin.site.register(Category)