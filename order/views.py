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
    client = Client.objects.get(User = user)
    order = Order( user = client, payment_status ='initiated', time_placed = timezone.now , quantity = len(selected_item_ids) , order_status ='placed' , discount=0 , price = total_cost)
    for id in selected_item_ids:
        item = (Items.objects.filter(ITEMID=id))[0]
        total_cost += item.item_price
        order.Items.add(item)
    request.session['order']=order.save()
    return render(request , 'order/finalize_order.html', {'item':item })

@login_required
def ordered(request):
    order = request.session['order']
    order.payment_status = 'done'
    order = order.save()
    return render(request , '/order/ordered.html', { 'order' : order })
