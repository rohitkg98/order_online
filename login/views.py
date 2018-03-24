from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect  #for redirecting on failed login/logiut
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from login.forms import *
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login(request):
   # c = {}
   # c.update(csrf(request))
    return render(request,'login.html')

def auth_view(request):
    uname = request.POST.get('username','')
    pword = request.POST.get('password','')
    user = auth.authenticate(username=uname , password= pword)  #check if username and password are correct, returns user if correct

    if user is not None:
        auth.login(request , user)
        return HttpResponseRedirect('/login/loggedin')  #redirect to logged in after logging in
    else:
        return HttpResponseRedirect('/login/invalidlogin')

@login_required(redirect_field_name = '/login/login')
def loggedin(request):
    user = request.user
    if user.groups.filter(name='Restaurant'):
        return HttpResponseRedirect('/restaurant/add_item')
    else:
        return HttpResponseRedirect("/order/select_res")

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def register(request):
    #if request.method == 'POST':
    client_group - Group.objects.get(name = 'Client')
    user_form = UserCreationForm(request.POST)
    client_form = ClientForm(request.POST)
    if user_form.is_valid() and client_form.is_valid():
        user_instance = user_form.save(commit =False)
        #user_instance.set_password(user_form.cleaned_data.get('password1'))
        user_instance.is_staff = True
        user_isntance.groups.add(client_group)
        user_instance.save()
        client_instance = client_form.save(commit = False)
        client_instance.User = user_instance
        client_instance.save()
        return render(request , 'registered.html',{'client_instance' : client_instance })
    else:
        return render(request,'register.html', {'user_form' : user_form , 'client_form':client_form})

def res_register(request):
    res_group = Group.objects.get(name = 'Restaurant')
    user_form = UserCreationForm(request.POST)
    res_form = RestaurantForm(request.POST)
    if user_form.is_valid() and res_form.is_valid():
        user_instance = user_form.save(commit = False)
        user_instance.is_staff = True
        #user_instance.set_password(user_form.cleaned_data.get('password1'))
        user_instance.save()
        user_instance.groups.add(res_group)
        user_instance.save()
        res_instance = res_form.save(commit =False)
        res_instance.User = user_instance
        res_instance.save()
        return render(request , 'res_registered.html' , { 'res_instance' : res_instance})
    else:
        return render(request , 'res_register.html' , {'user_form' : user_form , 'res_form' : res_form} )
