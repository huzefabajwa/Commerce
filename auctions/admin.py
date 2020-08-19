from django.contrib import admin
from .models import AuctionsList

# Register your models here.
class AuctionslistAdmin(admin.ModelAdmin):
    pass
admin.site.register(AuctionsList,AuctionslistAdmin)