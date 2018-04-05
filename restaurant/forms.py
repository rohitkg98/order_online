from django import forms
from restaurant.models import Items

class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [ 'item_name' , 'item_price' ] 
