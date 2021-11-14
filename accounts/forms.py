from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import fields
from .models import User
from django.contrib.auth.forms import AuthenticationForm




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



class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Stronge Password'})
    )
    password_confirm = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )
    class Meta:
        model = User
        fields = ('email', 'phone')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Email',
                }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter Your Phone Number',
                })
        }
        labels = {
            'email': 'Email',
            'phone': 'Phone',
            'password': 'Password',
            'password_confirm': 'Confirm Password'
        }

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords must match')
        return cd['password2']

    def clean_email(self):
        user_request_email = self.cleaned_data['email']
        db_check = User.objects.filter(email=user_request_email)
        if db_check.exists():
            raise forms.ValidationError('this email is exists')
        return user_request_email
    
    def clean_phone(self):
        user_request_phone = self.cleaned_data['phone']
        db_check = User.objects.filter(phone=user_request_phone)
        if db_check.exists():
            raise forms.ValidationError('this phone is exists')
        return user_request_phone

    def save(self, commit=True): # The save method(this method in ModelForm) is responsible for save form in DB.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user