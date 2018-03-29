from django.shortcuts import render
from login.models import Restaurant
from order.models import Items
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def select_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request , 'list_restaurants.html', {'restaurants' : restaurants} ) #checkbox for selecting list

@login_required
def show_items(request):
    res_id = request.POST.get('res_id','')
    items =[]
    restaurant = Restaurant.objects.filter(RID=res_id)
    for ID in restaurant.ITEMID:
        items.append((Items.objects.filter(ITEMID=ID))[0])
    return render(request , 'select_items.html', {'items':items} )

@login_required
def finalize_order(request):
    total_cost = 0
    selected_item_ids = request.POST.get('selected_item_ids','')
    user = request.user
    selected_items=[]
    for id in selected_item_ids:
        item = (Items.objects.filter(ITEMID=selected_item_ids))[0]
        selected_items.append(item)
        total_cost += item.price
    order = Order(items= selected_items , user = user, payment_status ='initiated', timeplaced = timezone.now , quantity = len(selected_items) , order_status ='placed' , discount=0 , price = total_cost)
    request.session['order']=order.save()
    return render(request , 'finalize_order.html', {'item':item })

@login_required
def ordered(request):
    order = request.session['order']
    order.payment_status = 'done'
    order = order.save()
    return render(request , 'ordered.html', { 'order' : order })
