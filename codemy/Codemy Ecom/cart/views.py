
from django.shortcuts import redirect, render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages



def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()   #Add Up  Totals - Django Wednesdays ECommerce 19
    return render(request, 'cartsummary.html', {'cart_products': cart_products, 'quantities': quantities,'totals':totals})    
   

def cart_add(request):
    #get the cart
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
         
        #save the session
        cart.add(product=product,quantity=product_qty)
        
        #get Cart quantity
        cart_quantity = cart.__len__()
        
        #return response
        # response = JsonResponse({'product name': product.name})
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, 'Product Added to the Cart successfully.')
        return response
    




#Delete Cart Items - Django Wednesdays ECommerce 18
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #get stuff
        product_id = int(request.POST.get("product_id"))

        #call delete item
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        messages.success(request, 'Product is Deleted from Cart!.')
        return response





#Update Shopping Cart - Django Wednesdays ECommerce 17
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        
        cart.update(product=product_id, quantity=product_qty)
        
        response = JsonResponse({'qty': product_qty})
        messages.success(request, 'Product update to the Cart successfully.')
        return response
        















# def cart_summary(request):
#     pass