from django.db import models

# Create your models here.



'''  এই মডেল ডেফিনিশন কোডটি ডি'জাঙ্গোতে পণ্যের তথ্য সংরক্ষণ করার জন্য ব্যবহৃত হয়। এই মডেলে চারটি ফিল্ড আছে: প্রোডাক্ট আইডি, প্রোডাক্ট নাম, বিবরণ এবং প্রকাশের তারিখ।   '''


class Product(models.Model):  
   
    product_id = models.AutoField   
    product_name = models.CharField(max_length=50)  
    price = models.IntegerField(default=0)
    
    category = models.CharField(max_length=50, default="")  

    subcategory = models.CharField(max_length=50, default="")  
     
       
    desc = models.CharField(max_length=1000) 
    pub_date = models.DateField() 
    image = models.ImageField(upload_to="shop/images",default= "")
    
    def __str__(self):
        return self.product_name
        # return super().__str__()





# model change korle command this "$ python manage.py makemigrations"

# model change na kore just method append korle command this "$ python manage.py migrate "








