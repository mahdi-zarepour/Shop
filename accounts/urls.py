from django.urls import path
from . import views



app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]