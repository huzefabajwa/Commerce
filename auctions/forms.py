from django import forms

from .models import AuctionsList


class auctions_list(forms.ModelForm):
    class Meta:
        model = AuctionsList
        fields = ('title','image','price',)
