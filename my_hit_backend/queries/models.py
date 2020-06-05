from django.db import models
from timetable.models import Course
from accounts.models import User

# Create your models here.
class Query(models.Model):
    STATUSES =(
        ('unread','unread'),
        ('read','read'),
        ('replied','replied'),
        )
    department = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length =255)
    query_description = models.TextField(null=True,blank=True)
    status = models.CharField(choices=STATUSES,max_length=50,default='unread')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    created_by =  models.ForeignKey(User,on_delete=models.CASCADE, related_name='created_by')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-timestamp",]
        verbose_name_plural = "Queries"

class Comment(models.Model):
    query = models.ForeignKey(Query,on_delete=models.CASCADE)
    commentator = models.ForeignKey(User,on_delete=models.CASCADE)
    reply_message = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.query.title
    
    class Meta:
        ordering = ["timestamp",]