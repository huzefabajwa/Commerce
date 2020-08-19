from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass

class AuctionsList(models.Model):
    title=models.CharField(max_length=3000)
    price=models.IntegerField()
    image=models.ImageField(upload_to='auctions/list',null=True,blank=True)

    def __str__(self):
        return f"{self.id}:{self.title}"


 
    