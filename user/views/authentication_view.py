from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.form import RegisterForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegisterForm()
            messages.success(request, "Account created successfully!")
            return redirect("login")

    context = {'form': form}
    return render(request, 'signup.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            name = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=name, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, "username or password not match")
    return render(request, "login.html")


def logout_user(request):
    print("Done")
    logout(request)
    return redirect("login")
