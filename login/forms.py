from django import forms
from login.models import Client
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password' ,'email' ,)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['User',] 
