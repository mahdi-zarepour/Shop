from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, Item
from cart.cart import Cart

# Zarinpal
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from suds.client import Client



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



MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "پرداخت فروشگاه آنلاین"
mobile = '09123456789'
CallbackURL = 'http://localhost:8000/orders/verify/'


@login_required
def payment(request, order_id, price):
    global amount, o_id
    o_id = order_id
    amount = price
    result = client.service.PaymentRequest(
        MERCHANT,
        amount,
        description,
        request.user.email,
        mobile, CallbackURL,
        )
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))



@login_required
def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order = Order.objects.get(id=o_id)
            order.paid = True
            order.save()
            messages.success(
                request,
                'Transaction was successful',
                'success',
                )
            return redirect('shop:all_product')

        elif result.Status == 101:
            return HttpResponse('Transaction submitted')
        else:
            return HttpResponse('Transaction failed.')
    else:
        return HttpResponse('Transaction failed or canceled by user')