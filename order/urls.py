from django.urls import path
from order.views import *
from django.conf.urls import url

urlpatterns = [
        url(r'^select_res/' ,select_restaurant ),
        url(r'^show_items/' , show_items),
        url(r'^finalize/', finalize_order),
        url(r'^ordered/', ordered),
        url(r'^view/',view_orders),
        ]
