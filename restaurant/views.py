from django.shortcuts import render
from restaurant.forms import ItemsForm
from login.models import Restaurant
from restaurant.models import Items
from django.contrib.auth.decorators import login_required
#Create your views here.
@login_required
def add_item(request):
    restaurant = Restaurant.objects.filter(User = request.user)[0]
    item_form = ItemsForm(request.POST , request.FILES)
    if item_form.is_valid():
        restaurant = restaurant.save()
        new_item = item_form.save(commit = True)
        new_item.image = request.FILES['image']
        new_item.save()
        restaurant = Restaurant.objects.filter(User = request.user)[0]
        restaurant.Items.add(new_item)
        restaurant = restaurant.save()
        return render(request , 'restaurant/item_added.html', {'new_item' : new_item , 'restaurant' : restaurant})
    print(item_form.errors)
    return render(request , 'restaurant/add_item.html', {'item_form' : item_form})

@login_required
def view_items(request):
    restaurant = Restaurant.objects.get(User = request.user)
    items = []
    for id in restaurant.ITEMID:
        items.append((Items.objects.filter(ITEMID=id))[0])
    return render(request , 'restaurant/view_items.html' , {'items' : items })
