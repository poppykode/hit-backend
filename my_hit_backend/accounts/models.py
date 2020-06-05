from django.db import models
from django.contrib.auth.models import AbstractUser
from timetable.models import Course


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='profile/',default='profile/HIT_logo.png',null=True,blank=True)
    course =models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True)
    is_student = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    student_number =  models.CharField(max_length =255,default='H1601575F')

    def __str__(self):
        return self.first_name + ' '+ self.last_name

    class Meta:
        ordering = ["-date_joined",]


