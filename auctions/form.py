from django.forms import ModelForm
from .models import Listing, Comment

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'starting_bid', 'image_url', 'category']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
