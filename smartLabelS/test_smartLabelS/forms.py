from django import forms
from .models import SignUp,  Product, Sites, Shipment

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp

class ProdugtForm(forms.ModelForm):
    class Meta:
        model = Product

class SitesForm(forms.ModelForm):
    class Meta:
        model = Sites

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment