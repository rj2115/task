from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from .models import *
from .forms import SignUpForm
import re
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate,  login,logout
# Create your views here.
def register(request):
   if request.method =="POST":
     fm= SignUpForm(request.POST)
     if fm.is_valid():
        messages.success(request,'Registered Successfully!')
        fm.save()
   else:
      fm= SignUpForm()
   return render(request,'new/register.html',{'form':fm})

def logins(request):
 if not request.user.is_authenticated:
   if request.method =="post":
      fm=AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
         uname=fm.cleaned_data['username']
         upass=fm.cleaned_data['password']
         user = authenticate(username=uname,password=upass)
         if user is not None:
            login(request, user)
            messages.success(request,'LOGGED IN SUCCESFULLY!!!')
              
            return HttpResponseRedirect('/profile/')
        
   else:
         
      fm= AuthenticationForm()
   return render(request,'new/login.html',{'form':fm})
 else:
    return HttpResponseRedirect('/profile/')

def new_profile(request):
 if request.user.is_authenticated:
   
   return render(request,'new/profile.html',{'name':request.user,})
 else:
    return HttpResponseRedirect('/login/')
def Search(request):
   
   return render(request,'new/search.html')
def ulogout(request):
   logout(request)
   return HttpResponseRedirect('/login/')



def hi(request):

   data=request.POST.get('input')
   if request.method=="POST":
   
   
    val=request.POST['filter']
    if val=="num_100":
      match=re.findall(r"\d(3)\d*",data)
      print(match)
      return render(request,'new/validations.html',{'filter':val,'validation':match})
    
   
   
    elif val=="extract_date":
      match=re.findall(r"\d(4)-\d(2)-\d(2)",data)
      print(match)
      return render(request,'new/validations.html',{'filter':val,'validation':match})
    
    
    elif val=="quote_string":
      match=re.findall(r'\'[a-zA-Z]+\'',data)
      print(match)
      return render(request,'new/validations.html',{'filter':val,'validation':match})
   
   
    elif val=="validate_email":
       pat="[a-z A-Z 0-9]+@[a-z]+\.(com|edu|net)"
       if (re.search(pat,data)):
          print("Valid Email")
          return render(request,'new/validations.html',{'filter':val,'validation':'Valid Email'})
       else:
          print("Not a valid email!")
          return render(request,'new/validations.html',{'filter':val,'validation':'Not a  valid email!'})


       
    elif val=="ip_address":
       pat=r"\d*\.\d*\.\d*\.\d*"
       if re.search(pat,data):
        print("Valid")  
        return render(request,'new/validations.html',{'filter':val,'validation':'Valid'})
       else:
        print("Not a Valid ip address")
        return render(request,"new/validations.html",{'filter':val,'validation':'Not a Valid ip address'})

    elif val=="mac_address":
       pat=r"[A-Z0-9](2)\.[A-Z0-9](2)\.[A-Z0-9](2)\.[A-Z0-9](2)\.[A-Z0-9](2)\.[A-Z0-9](2)"
       if re.search(pat,data):
        print("Valid")  
        return render(request,'new/validations.html',{'filter':val,'validation':'Valid'})
       else:
        print("Not a Valid MAC address")
        return render(request,"new/validations.html",{'filter':val,'validation':'Not a Valid MAC address'})
    


   else:
       return render(request,'new/validations.html',{'filter':"no validation is selected",'validation':'no radio button selected'})
    

   # print(data)
   
   
      
    #  pat=re.compile(r'0-9(3)')
     # if re.search(pat,data):
       #  matches=