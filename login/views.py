from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect  #for redirecting on failed login/logiut
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from login.forms import *
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
    return render(request,'loggedin.html')

def invalidlogin(request):
    return render(request,'invalidlogin.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def register(request):
    #if request.method == 'POST':
    user_form = UserForm(request.POST)
    client_form = ClientForm(request.POST)
    if user_form.is_valid():
        return HttpReponseRedirect('/login/registered')
    else:
        return render(request,'register.html', {'user_form' : user_form , 'client_form':client_form})

def registered(request):
    user = User.objects.create_user(username = request.POST.get('username','') , password = request.POST.get('password','') , email = request.POST.get('email',''))
    user.is_staff = True
    user.first_name = request.POST.get('fname','')
    user.last_name = request.POST.get('lname' ,'')
    user.save()
    client = Client(User = user , phone_number = request.POST.get('phone_number','') , state = request.POST.get('state',''), name = user.first_name+' '+user.last_name , city = request.POST.get('city','') , address = request.POST.get('address',''))
    client.save()
    return render(request , 'registered.html')
