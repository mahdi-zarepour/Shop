from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Item
from cart.cart import Cart



class OrderCreate(LoginRequiredMixin, CreateView):
     login_url = 'accounts:login'

     def get(self, request, *args, **kwargs):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            Item.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
                )
            cart.clear()
            return redirect('order:order_detail', order.id)



class OrderDeteil(LoginRequiredMixin, DetailView):
     login_url = 'accounts:login'

     def get(self, request, *args, **kwargs):
         order = get_object_or_404(Order, pk=kwargs['order_id'])

         if order.user != request.user:
             return redirect("shop:all_product")

         return render(request, 'order/order.html', {'order': order})
