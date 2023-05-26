from django.db import models

# Create your models here.

class Students(models.Model):
    
    
    first_name = models.CharField(max_length=50)
    
    last_name = models.CharField(max_length=50)
    
    division = models.CharField(max_length=10)
    
    marks = models.IntegerField()
