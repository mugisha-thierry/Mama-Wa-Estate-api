from .models import Store
from django import forms

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields =  ('name','service','location')