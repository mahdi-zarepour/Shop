from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import Product, Category



class AllProduct(ListView):
    queryset = Product.objects.filter(available=True)
    context_object_name = 'products'
    template_name = 'shop/all_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(is_subcategory=False)
        return context 



class ProductDetail(DetailView):
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    def get_queryset(self, **kwargs):
        return Product.objects.filter(slug__iexact=self.kwargs['slug'])



class Category_Product_List(ListView):
    def get_queryset(self, **kwargs):
        return Category.objects.filter(slug=self.kwargs['category'])
    context_object_name = 'categories'
    template_name = 'shop/category_product_list.html'

