from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length =255)
    date = models.DateTimeField()
    description = models.TextField(null=True,blank=True)
    location =  models.CharField(max_length =255,null=True,blank=True)
    image = models.ImageField(upload_to='events')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp",]
