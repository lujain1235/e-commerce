from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import user
from django.contrib.auth.models import User, auth
from datetime import datetime



def userlogin(request):
    try:
        if request.method == "POST":
            return perform_login(request) 
        return render(request, "base.html")
    except KeyError as e:
        messages.info(request, f"{e} is required")
        return redirect("")


def perform_login(request):
    user = auth.authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is not None:
        auth.login(request, user)
        return redirect("/")
    else:
        messages.info(request, "Invalid credentials")
        return redirect("/")


def validate(request, *args):
    map(lambda x: request.POST[x], args)


def register(request):
    try:
        if request.method == 'POST':
            validate(("email", "password1", "password2"))
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 != password2:
                messages.info(request, "Password does not Not Match!")
                return redirect("/")

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email is already taken!")
                return redirect("/")

            User.objects.create_user(
                username=request.POST['username'],
                email=email,
                password=password1
            )
            return redirect('/')
        else:
            return redirect("/")
    except KeyError as e:
        messages.info(request, f"{e} is required")
        return redirect('/')
    except Exception as e:
        messages.info(request, f"Failed {e}")
        return redirect('/')

def userdetails(request, u):
    try:
        myuser = user.objects.get(username=u)
        return render(request, 'HTML/UserDetails.html', {"myuser": myuser})
    except Exception as e:
        messages.info(request, f"{e}Invalid Credentitial")
        return redirect('/')

def edituser(request):
    try:
        if request.method == "POST":
            required_fields = ["id", "name", "username", "phone", "email", "address", "dob", "gender", "profession", "status"]
            if all(request.POST.get(field) for field in required_fields):
                try:
                    users = user.objects.get(id=request.POST.get("id"))
                except user.DoesNotExist:
                    messages.info(request, "User not found.")
                    return redirect('/')

                users.name = request.POST.get("name")
                users.username = request.POST.get("username")
                users.phone = request.POST.get("phone")
                users.email = request.POST.get("email")
                users.address = request.POST.get("address")
                users.dob = datetime.strptime(request.POST.get("dob"), "%Y-%m-%d")

                users.gender = request.POST.get("gender")
                users.profession = request.POST.get("profession")
                users.status = request.POST.get("status")
                users.save()
                return HttpResponseRedirect(f"/accounts/User/{users.username}")
            else:
                messages.info(request, "Missing fields")
                return redirect('/')
    except Exception as e:
        messages.info(request, f"{e}")
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect("/")
