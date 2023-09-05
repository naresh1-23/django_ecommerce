from django.shortcuts import render, redirect
from django.contrib.auth import login , logout, authenticate
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password


def loginView(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            messages.warning(request, "Fields cannot be empty")
        else:
            user = authenticate(request, username= username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request,"Login successfully")
                return redirect("home")    
            else:
                messages.warning(request, "username or password didn't matched")
        return render(request, "login.html")
    else:
        return render(request, 'login.html')
    
def SignupView(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        hased_pass = make_password(password1)
        if username == '' or email == '' or password1 == '' or password2 == '' or contact == '':
            messages.warning(request, "Fields cannot be empty")
        else:
            if password1 != password2:
                messages.warning(request, "Password didn't matched")
            else:
                user = CustomUser.objects.filter(username = username).first()
                if user:
                    messages.warning(request, "Username already exists")
                else:
                    userdata = CustomUser.objects.create(username = username, email = email,contact = contact, password = hased_pass)
                    userdata.save()
                    messages.success(request, "Successfully registered")
                    return redirect("login")
        return render(request, 'signup.html')
    else:
        return render(request, "signup.html")
    
@login_required            
def logoutView(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('login')
    