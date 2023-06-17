from django.contrib.auth.models import AbstractUser
from django.db import models

from .id import Id


class User(AbstractUser):
    pass


class Listings(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    bid = models.IntegerField()
    photo_url = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        self.id = Id().generate()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    listing_id = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    
    def __str__(self):
        return self.text
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(Listings)

    def __str__(self):
        return f"{self.user}'s Watchlist"