from django import forms
from shoppingApp.models import Product
from shoppingApp.models import Cart

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class CartForm(forms.ModelForm):
	class Meta:
		model = Cart
		fields = "__all__"