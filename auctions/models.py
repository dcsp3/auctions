from django.contrib.auth.models import AbstractUser
from django.db import models

from .id import Id


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Listing(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    highest_bid = models.DecimalField(max_digits=10, decimal_places=2)
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    image_url = models.CharField(max_length=500, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not Listing.objects.filter(id=self.id).exists():
            self.id = Id().generate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user}'s Bid on {self.listing.title}"
    

class Comment(models.Model):
    listing_id = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=300)
    
    def __str__(self):
        return self.comment_text
    

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(Listing)

    def __str__(self):
        return f"{self.user}'s Watchlist"