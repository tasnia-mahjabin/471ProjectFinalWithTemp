from django import forms
from .models import Product

class updateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'catagory', 'brand', 'country', 'quantity', 'description', 'img']
