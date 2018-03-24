from django import forms
from login.models import Client,Restaurant
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password' ,'email' ,)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['User','USERID',]

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name','address','state','city', )
