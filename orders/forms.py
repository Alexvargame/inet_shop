from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

    class Meta:
        model=Order
        fields=('username','name','email','phone_number')











