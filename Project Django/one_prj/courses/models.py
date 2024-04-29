from django.db import models

# Create your models here.

class PythonCourse(models.Model):
    caption1 = models.CharField(max_length=100)
    video1 = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption1
    
    
class DjangoCourse(models.Model):
    caption2 = models.CharField(max_length=100)
    video2 = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption2
    
    
class RequestsCourse(models.Model):
    caption3 = models.CharField(max_length=100)
    video3 = models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption3
