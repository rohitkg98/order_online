from django.urls import path
from login.views import login, auth_view, logout, loggedin, invalidlogin, register, registered
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
        url(r'^login/$', login),
        url(r'^auth/$', auth_view),
        url(r'^logout/$', logout),
        url(r'^loggedin/$', loggedin),
        url(r'^invalidlogin/$', invalidlogin),
        url(r'^register/$',register),
        url(r'^registered/$',registered)
        ]
