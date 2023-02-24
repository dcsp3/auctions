from django.forms import ModelForm
from .models import Listings, Comments

class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'bid']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
