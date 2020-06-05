from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length =255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp",]

class Subject(models.Model):
    DAYS =(
        ('monday','Monday'),
        ('tuesday','Tuesday'),
        ('wednesday','Wednesday'),
        ('thursday','Thursday'),
        ('friday','Friday'),
        ('saturday','Saturday'),
        ('sunday','Sunday'),)
    course =models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length =255)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    venue = models.CharField(max_length =255)
    day = models.CharField(max_length=30,choices=DAYS,default='monday')
    time = models.TimeField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-timestamp",]

class Timetable(models.Model):
    course =models.ForeignKey(Course,on_delete=models.CASCADE)
    file_name = models.FileField(upload_to='timetables/')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course.name
    
    class Meta:
        ordering = ["-timestamp",]




