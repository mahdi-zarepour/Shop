from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User



class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='password confirm', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone')

    
    def clean_password_confirm(self):
        cd = self.cleaned_data
        if [cd['password'] != cd['password_confirm']]:
            raise forms.ValidationError('Password Must Match')
        return cd['password_confirm']

    
    def save(self, commit=True): # The save method(this method in ModelForm) is responsible for save form in DB.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField() # for show hash password
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password')


    def clean_password(self): # در خود فیلد به مقدار اولیش دسترسی نداریم، به همین دلیل از کلین استفاده میکنیم
        return self.initial['password'] # مقدار اولیه پسورد