from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import auctions_list

from django.template import RequestContext
from .models import AuctionsList

from .models import User



def index(request):
    return render(request, "auctions/index.html")


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

def auctionslist(request):
        AuctionsLists=AuctionsList.objects.all()
        return render(request, "auctions/index.html",{
               "AuctionsLists" : AuctionsLists
        })

def imageupload(request):
        if request.method == 'POST':
            form = auctions_list(request.POST, request.FILES)
            if form.is_valid():
               form.save()
               return HttpResponseRedirect("auctionslist")
        else:
            form = auctions_list()    
        return render(request, "auctions/upload.html",{
            "form":form
        })

def auction(request, AuctionsList_id):
        AuctionsLists=AuctionsList.objects.filter(id=AuctionsList_id)
        return render(request, "auctions/auction.html",{
               "AuctionsLists" : AuctionsLists
        })


