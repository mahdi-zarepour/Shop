from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .cart import Cart
from .forms import CartAddForm
from shop.models import Product


class CartDetail(View):
    template_name = 'cart/cart_detail.html'

    def get(self, request):
        cart = Cart(request)
        return render(request, self.template_name, {'cart': cart})

    def post(self, request, *args, **kwargs):
        return redirect('shop:all_product')



class CartAdd(View):
    # CartAdd: get product and quantity, and send to Cart.py
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        form = CartAddForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cart.add(product, cleaned_data['quantity'])
        return redirect('cart:cart_detail')

    def get(self, request):
        return redirect('shop:all_product')



class CartRemove(View):
    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        cart.remove(product)
        return redirect('cart:cart_detail')
