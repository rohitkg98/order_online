from django.shortcuts import render
from restaurant.forms import ItemsForm
from login.models import Restaurant
from restaurant.models import Items
from django.contrib.auth.decorators import login_required
#Create your views here.
@login_required
def add_item(request):
    restaurant = (Restaurant.objects.filter(User = request.user))[0]
    item_form = ItemsForm(request.POST , request.FILES)
    if item_form.is_valid():
        new_item = item_form.save(commit = False)
        new_item.image = request.FILES['image']
        item = new_item.save()
        restaurant.ITEMID.add(item.ITEMID)
        restaurant = restaurant.save()
        return render(request , 'item_added.html', {'new_item' : item , 'restaurant' : restaurant})
    print(item_form.errors)
    return render(request , 'add_item.html', {'item_form' : item_form})
@login_required
def view_items(request):
    restaurant = Restaurant.objects.get(User = request.user)
    items = []
    for id in restaurant.ITEMID:
        items.append((Items.objects.filter(ITEMID=id))[0])
    return render(request , 'view_items.html' , {'items' : items })
