from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


def signnewuser(req):
    print(req.method)
    if req.method == "POST":
        print("Successfully started")
        if req.POST.get("password1") == req.POST.get("password2"):
            try:
                saveuser = User.objects.create_user(req.POST.get("username"), password=req.POST.get("password1"))
                saveuser.save()
                return render(req, "signup.html", {"form": UserCreationForm(), "info":f"THe user {req.POST.get('username')} is saved successfully"})
            except:
                return render(req, "signup.html", {"form": UserCreationForm(), "error":f"THe user{req.POST.get('username')} is already added to the db"})

        else:
            return render(req, "signup.html", {"form": UserCreationForm(), "error":f"THe user {req.POST.get('username')} is not added due to incoorectly matched passwords"})

    else:
        return render(req, "signup.html", {'form': UserCreationForm})
    
def loginuser(req):
    if req.method == "POST":
        loginsuccess = authenticate(req, username = req.POST.get("username"), password=req.POST.get("password"))
        if loginsuccess is None:
            return render(req, "login.html", {'form': AuthenticationForm, "error": "the username and password is wrong..."})
        else:
            login(req, loginsuccess)
            return redirect("/products")
    else:
        return render(req, "login.html" , {'form':AuthenticationForm})
        
def logoutuser(req):
    if req.method =="POST":
        logout(req)
        return redirect("/auth/login")

