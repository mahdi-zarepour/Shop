from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('create/', views.OrderCreate.as_view(), name='order_create'),
    path('<int:order_id>/', views.OrderDeteil.as_view(), name='order_detail'),
]