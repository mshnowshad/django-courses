from .cart import Cart

# Create context processor so our cart can work on all pages of the site
def userauth(request):
	# Return the default data from our Cart
	return {'cart': Cart(request)}