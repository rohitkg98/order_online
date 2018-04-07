from django.shortcuts import render
from login.models import Restaurant, Client
from restaurant.models import Items
from order.models import Order
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def select_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request , 'order/list_restaurants.html', {'restaurants' : restaurants} ) #checkbox for selecting list

@login_required
def show_items(request):
    res = Restaurant.objects.get(RID=request.POST.get('res_id'))
    items=[]
    for item in res.Items.all():
        items.append(item)
    return render(request , 'order/select_items.html', {'items':items} )

@login_required
def finalize_order(request):
    total_cost = 0
    selected_item_ids = request.POST.getlist('selected_item_ids')
    user = request.user
    item =[]
    client = Client.objects.get(User = user)
    order = Order.objects.create( user = client, quantity = len(selected_item_ids) , order_status ='placed' , discount=0 , price = total_cost)
    for id in selected_item_ids:
        temp = Items.objects.filter(ITEMID=id)[0]
        item.append(temp)
        total_cost += temp.item_price
    order.Items.set(item)
    order.price = total_cost
    order.payment_status = True
    order.save()
    return render(request , 'order/finalize_order.html', {'order' : order ,'total_cost' : total_cost})
@login_required
def ordered(request):
        return render(request , 'order/ordered.html')
@login_required
def view_orders(request):
    orders = Order.objects.filter(user = Client.objects.get(User =request.user ))
    return render(request , 'order/view_orders.html' , {'orders' : orders })
