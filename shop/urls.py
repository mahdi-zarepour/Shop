from django.urls import path
from . import views



app_name = 'shop'
urlpatterns = [
    path('', views.all_product, name='all_product'),
]