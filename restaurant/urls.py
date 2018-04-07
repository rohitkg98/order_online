from django.conf.urls import url
from restaurant.views import add_item, view_items, remove_item, view_orders
urlpatterns = [
        url(r'^/add_item/',add_item),
        url(r'^/view_items/',view_items),
        url(r'^/remove/',remove_item),
        url(r'^/view_orders/',view_orders),
        ]
