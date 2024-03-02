from store.models import Product,Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        #get request
        self.request = request
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart



    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = int(quantity)
        if product_id in self.cart:
            # If product already exists in cart, update quantity
            self.cart[product_id] += product_qty
        else:
            self.cart[product_id] = product_qty
        self.session.modified = True


        # Cart Persistence on Logout  - Django Wednesdays ECommerce 27
        if self.request.user.is_authenticated :
            # get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            #convert
            carty = str(self.cart)
            carty = carty.replace("\'","\"")
            #save carty to the Profile Model
            current_user.update(old_cart=str(carty))


    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        
        return self.cart
    
    


    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)
        ourcart = self.cart
        ourcart[product_id] = product_qty
        
        self.session.modified = True
        
        thing = self.cart
        return thing



    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value
        return total
