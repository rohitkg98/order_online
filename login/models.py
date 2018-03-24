from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
import uuid
from restaurant.models import *
# Create your models here.
class Client(models.Model):
    USERID = models.UUIDField(primary_key = True , default = uuid.uuid4)
    User = models.OneToOneField(User , on_delete=models.CASCADE )
    phone_number = models.CharField(validators = [ MinLengthValidator(10), MaxLengthValidator(13)] ,max_length=13) #add a phone number regex for validation
    state = models.CharField( max_length=20 )
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=100)


class Restaurant(models.Model):
    RID = models.UUIDField( primary_key=True , default = uuid.uuid4 ) #add validator
    User = models.OneToOneField(User , on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    state = models.CharField(max_length = 20)
    ITEMID = models.ManyToManyField(Items )
    city = models.CharField( max_length = 20)
    ratings = models.IntegerField(default = 0 )
