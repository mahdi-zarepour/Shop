from django import forms
from django.forms.widgets import NumberInput



class CartAddForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=NumberInput(attrs={'class': 'form-control col-md-3', 'placeholder': '1 ... 10'})
    )