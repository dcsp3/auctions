from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .form import ListingForm, CommentForm
from .models import User, Listings, Comments, Watchlist, Category


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all()
    })

    
def create(request):
    form = ListingForm

    categories = Category.objects.all()

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('index')
    
    return render(request, "auctions/create.html", {
        "form": form,
        "categories": categories
    })


def listing(request, id):
    listing = Listings.objects.get(id=id)

    is_added_to_watchlist = False
    if request.user.is_authenticated:
        watchlist = Watchlist.objects.filter(user=request.user, listings=listing).exists()
        if watchlist:
            is_added_to_watchlist = True

    form = CommentForm
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.listing_id = id
            form.save()
            return redirect('listing', id)
            
    comments = Comments.objects.filter(listing_id=id)

    return render(request, "auctions/listing.html", {
        "listing": listing,
        'is_added_to_watchlist': is_added_to_watchlist,
        "comments": comments[::-1],
        "form": form,
    })


def add_to_watchlist(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)
    watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    watchlist.listings.add(listing)

    return redirect("listing", listing_id)


def watchlist(request):
    try:
        watchlist = Watchlist.objects.get(user=request.user)
        watchlist_items = watchlist.listings.all()
    except Watchlist.DoesNotExist:
        watchlist_items = []

    context = {
        "watchlist_items": watchlist_items,
    }

    return render(request, "auctions/watchlist.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
