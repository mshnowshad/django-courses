from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):  #ADMIN PANEL CUSTOMIZED OF PRODUCTLIST
    list_display = ('id','name','price','published','created')
    list_display_links = ('id','name')  #eita diye product edit kora jay
    list_filter = ('price','created')
    list_editable = ('published',)
    search_fields = ('name','price')
    
    
admin.site.register(Product,ProductAdmin)
