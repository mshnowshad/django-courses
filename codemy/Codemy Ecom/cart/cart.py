from store.models import Product, Profile

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request
        # Initialize cart from session, or an empty dictionary if not present
        self.cart = self.session.get('cart', {})

    def add(self, product, quantity):
        product_id = str(product.id)
        # Update quantity if product already exists in cart, otherwise add it
        if product_id in self.cart:
            self.cart[product_id] += quantity
        else:
            self.cart[product_id] = quantity
        # Save cart to session and mark session as modified
        self.session['cart'] = self.cart
        self.session.modified = True
        # Update user's old_cart attribute if user is authenticated
        if self.request.user.is_authenticated:
            current_user = Profile.objects.get(user=self.request.user)
            current_user.old_cart = self.cart
            current_user.save()

    def cart_total(self):
        # Retrieve products from cart
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total = 0
        # Calculate total price
        for product in products:
            total += product.get_price() * self.cart[str(product.id)]
        return total

    def __len__(self):
        # Return the number of items in the cart
        return len(self.cart)

    def get_prods(self):
        # Retrieve products from cart
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        # Return the dictionary containing product IDs and their quantities
        return self.cart

    def update(self, product, quantity):
        # Update quantity of a product in the cart
        product_id = str(product.id)
        self.cart[product_id] = quantity
        # Mark session as modified
        self.session.modified = True
        # Update user's old_cart attribute if user is authenticated
        if self.request.user.is_authenticated:
            current_user = Profile.objects.get(user=self.request.user)
            current_user.old_cart = self.cart
            current_user.save()
        return self.cart

    def delete(self, product):
        # Remove a product from the cart
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        # Mark session as modified
        self.session.modified = True
        # Update user's old_cart attribute if user is authenticated
        if self.request.user.is_authenticated:
            current_user = Profile.objects.get(user=self.request.user)
            current_user.old_cart = self.cart
            current_user.save()
