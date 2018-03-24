from django.shortcuts import render
from restaurant.forms import ItemsForm
from login.models import Restaurant
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#Create your views here.
@login_required
def add_item(request):
    restaurant = Restaurant.objects.get(user = request.user)
    item_form = ItemsForm(request.POST)
    if item_form.is_valid():
            new_item = item_form.save(commit = False)
            new_item.timestamp = timezone.now
            new_item.save()
            restaurant.ITEMID.add(new_item.ITEMID)
            restaurant.save()
            return render(request , 'item_added.html')
    return render(request , 'add_item.html')

