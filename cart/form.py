from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class AddProductToCartForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=20)
    override = forms.BooleanField(required=False, initial = False, widget=forms.HiddenInput)