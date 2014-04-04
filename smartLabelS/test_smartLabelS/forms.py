from django import forms
from .models import SignUp, CreateF

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        
        
class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateF