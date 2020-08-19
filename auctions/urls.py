from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("auctionslist", views.auctionslist, name="auctionslist"),
    path("imageupload", views.imageupload, name="imageupload"),
    path("<int:AuctionsList_id>", views.auction, name="auction")
    
]
