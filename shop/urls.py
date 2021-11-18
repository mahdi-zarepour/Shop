from django.urls import path
from . import views



app_name = 'shop'
urlpatterns = [
    path('', views.AllProduct.as_view(), name='all_product'),
    path('<slug:slug>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<slug:category>/', views.Category_Product_List.as_view(), name='category_product_list'),
]