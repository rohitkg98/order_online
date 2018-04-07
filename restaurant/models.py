from django.db import models
import uuid
# Create your models here.

class Items(models.Model):
    ITEMID = models.UUIDField(primary_key = True , default = uuid.uuid4)  #come up with a regex for itemid
    item_name = models.CharField(max_length = 20)
    image = models.ImageField(upload_to = 'images/' , default='images/none/noimg.png')
    item_price = models.PositiveIntegerField()
    reviews = models.CharField(max_length=100)
