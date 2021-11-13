from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User



class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='password confirm', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone')

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords must match')
        return cd['password2']

    
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