from django import forms
from ..models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control p-2'}))
    category = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control p-2'}))
    brand = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control p-2'}))
    weight = forms.DecimalField(max_digits=10,decimal_places=2, widget=forms.NumberInput(attrs={'class':'form-control p-2'}))
    price = forms.DecimalField(max_digits=10,decimal_places=2, widget=forms.NumberInput(attrs={'class':'form-control p-2'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control p-2'}))
    class Meta:
        model = Product
        fields = ('__all__')