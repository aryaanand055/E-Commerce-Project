from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
from django.contrib import messages

def signnewuser(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, f"The user {user.username} is registered successfully.")
            return redirect('products')  # Redirect to the home page or any other page you prefer
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        form = CustomUserCreationForm()

    return render(request, "signup.html", {"form": form})


def loginuser(req):
    if req.method == "POST":
        loginsuccess = authenticate(req, username=req.POST.get("username"), password=req.POST.get("password"))
        if loginsuccess is None:
            form = AuthenticationForm()
            return render(req, "login.html", {'form': form, "error": "The username and password are incorrect..."})
        else:
            login(req, loginsuccess)
            return redirect("/products")
    else:
        form = AuthenticationForm()  # Instantiate AuthenticationForm
        return render(req, "login.html", {'form': form})    
def logoutuser(req):
    if req.method =="POST":
        logout(req)
        return redirect("/auth/login")

