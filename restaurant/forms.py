from django import forms
from restaurant.models import Items

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        exclude = ('ITEMID','review',)
