from django.shortcuts import render
from login.models import Restaurant
from order.models import Items
from django.utils import timezone
# Create your views here.

def select_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request , 'list_restaurants.html') #checkbox for selecting list

def show_items(request):
    res_id = request.POST.get('res_id','')
    items =[]
    restaurant = Restaurant.objects.get(RID=res_id)
    for ID in restaurant.ITEMID:
        items.append(Items.objects.get(ITEMID=ID))
    return render(request , 'select_items.html')

def finalize_order(request):
    total_cost = 0
    selected_items = request.POST.get('selected_items','')
    user = request.POST.get('user','')
    for item in selected_items:
        total_cost += item.price
    order = Order(items= selected_items , user = user, payment_status ='initiated', timeplaced = timezone.now , quantity = len(selected_items) , oorder_status ='placed' , discount=0 , price = total_cost)
    order.save()
    return render(request , 'finalize_order.html')

def ordered(request):
    order = request.POST.get('order','')
    order.payment_status = 'done'
    order.save()
    return render(request , 'ordered.html')
