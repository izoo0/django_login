from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#from django.views.generic import ListView

# Create your views here.

def login_auth(request):
     if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request,user)
               return redirect('home')
          else:
               messages.success(request,("There was an error loging in try again"))
               return redirect('login-user')
     else:
          return render(request, "login.html",{})
     
def home_view(request):
     return render(request,"dash.html",{})