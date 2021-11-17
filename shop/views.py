from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Product


class AllProduct(ListView):
    queryset = Product.objects.filter(available=True)
    context_object_name = 'products'
    template_name = 'shop/all_products.html'


class ProductDetail(DetailView):
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    def get_queryset(self, **kwargs):
        return Product.objects.filter(slug__iexact=self.kwargs['slug'])