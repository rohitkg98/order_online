from django.shortcuts import render
from restaurant.models import ItemsForm
from dajngo.utils import timezone
#Create your views here.

def add_item(request):
    item_form = ItemsForm(request.POST)
    if item_form.is_valid():
            current_form = item.save(commit = False)
            current_form.timestamp = timezone.now
            current_form.save()
            return render(request , 'item_added.html')
    return render(request , 'add_item.html')

