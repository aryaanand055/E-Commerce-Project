from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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