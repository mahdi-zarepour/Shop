from django.contrib.auth import views as auth_views



class LoginUser(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True



class LogoutUser(auth_views.LogoutView):
    redirect_authenticated_user = True
    
