from django.db import models
from login.models import *
from restaurant.models import *
from django.utils import timezone
import uuid
from json import JSONEncoder

# Create your models here.
class Order(models.Model):
    ORDERID = models.UUIDField( primary_key=True , default = uuid.uuid4)
    Items = models.ManyToManyField(Items,symmetrical = False)   #Foreign key to Items
    user = models.ForeignKey(Client , on_delete = models.SET_NULL , null = True)  #Foreign key to Client
    payment_status = models.BooleanField(default = False)
    time_placed = models.DateTimeField( default = timezone.now)
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=20) #add choices
    discount = models.IntegerField()
    price = models.IntegerField()
