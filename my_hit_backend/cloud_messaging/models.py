from django.db import models
from accounts.models import User

# Create your models here.
class CloudMessaging(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    fcm_token =  models.CharField(max_length =255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp",]

