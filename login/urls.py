from django.urls import path
from login.views import  auth_view, loggedin, invalidlogin, register, res_register, logout
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
        url(r'^login/$',auth_views.login , name ='login'),
        url(r'^auth/$', auth_view , name = 'logout'),
        url(r'^logout/$', logout),
        url(r'^loggedin/$', loggedin),
        url(r'^invalidlogin/$', invalidlogin),
        url(r'^register/$',register),
        url(r'^res_register/$',res_register)
        ]
