from django import forms
from .models import SignUp,  Product, Sites, Shipment, ShipmentMonitor

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

class ShipmentMonitorForm(forms.ModelForm):
    class Meta:
        model = ShipmentMonitor