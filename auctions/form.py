from django.forms import ModelForm
from .models import Listings

class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 'description', 'bid']
