from django.shortcuts import render


def all_product(request):
    return render(request, 'shop/all_product.html')
