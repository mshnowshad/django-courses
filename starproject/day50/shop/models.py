from django.db import models
from .models import *
# Create your models here.



'''  এই মডেল ডেফিনিশন কোডটি ডি'জাঙ্গোতে পণ্যের তথ্য সংরক্ষণ করার জন্য ব্যবহৃত হয়। এই মডেলে চারটি ফিল্ড আছে: প্রোডাক্ট আইডি, প্রোডাক্ট নাম, বিবরণ এবং প্রকাশের তারিখ।   '''

class Category(models.Model):
    name = models.CharField(max_length=50, default='')
    
    def __str__(self):
        return self.name
        

class Product(models.Model):  
   
    id = models.AutoField(primary_key=True, default=None)  
    product_name = models.CharField(max_length=50)  
    price = models.IntegerField(default=0)   
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)  
    desc = models.TextField() 
    pub_date = models.DateField() 
    image = models.ImageField(upload_to="shop/images",default= "")
    
    def __str__(self):
        return self.product_name
        # return super().__str__()


class Contact(models.Model): 
    msg_id = models.AutoField(primary_key=True, default=None) 
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    
    
    def __str__(self):
        return self.name
        # return super().__str__()





# model change korle command this "$ python manage.py makemigrations"

# model change na kore just method append korle command this "$ python manage.py migrate "








