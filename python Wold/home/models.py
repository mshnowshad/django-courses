from django.db import models
from datetime import *

# Create your models here.


class Product(models.Model):
   name = models.CharField(max_length=200,null=False,blank=True)
   category = models.CharField(max_length=50,null=False,blank=True)
   
   price = models.DecimalField(max_digits=5, decimal_places=2)
   description = models.TextField()
   published = models.BooleanField(default=True)
   created = models.DateTimeField(default=datetime.now,blank=False)
   image = models.ImageField(upload_to='home/images',default="")
   
   
   def __str__(self):
       return self.name
   


    

 
 
 
     