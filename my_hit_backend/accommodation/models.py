from django.db import models
from accounts.models import User

# Create your models here.
class Accomodation(models.Model):
    name = models.CharField(max_length =255)
    price = models.IntegerField(default = 0.0)
    available_spaces=  models.IntegerField()
    available = models.BooleanField(default = True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp",]

class Booking(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    accomodation =models.ForeignKey(Accomodation,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.id +' '+ self.accomodation.id

    class Meta:
        ordering = ["-timestamp",]