from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods

@require_http_methods(["GET","POST"])
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("user:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "user/login.html", context)

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)

@require_POST
def logout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect("index")