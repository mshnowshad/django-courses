from django.contrib import admin
from .models import *

#Extend User Profiles - Django Wednesdays ECommerce 24
from django.contrib.auth.models import User


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'date')
    list_display_links = ('id', 'name')
    list_filter = ('price', 'date', 'category')  # Corrected to tuple format
    search_fields = ('name', 'price', 'category__name')  # Corrected to tuple format with category__name


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email')
    list_display_links = ('id', 'first_name', 'last_name')
    list_filter = ('address',)  # Corrected to tuple format
    search_fields = ('email', 'phone', 'first_name', 'last_name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'phone', 'quantity')
    list_display_links = ('id', 'product')
    list_filter = ('product', 'date', 'phone')  # Corrected to tuple format
    search_fields = ('customer__first_name', 'customer__last_name', 'phone', 'product__name')  # Corrected to tuple format with customer__first_name and customer__last_name




    
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)


admin.site.register(Profile)


# Mix profile info and user info
class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)

