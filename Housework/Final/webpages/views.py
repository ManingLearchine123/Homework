from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Game
from .serializers import GameSerializer as S, DetailSerializer as DS, UserSerializer as US
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .bots import chatbot
from django.contrib.auth import login as l
from django.contrib.auth import logout as lo
from django.contrib.auth.models import User
from django.contrib.auth.forms import (AuthenticationForm as AF, PasswordChangeForm as CPF)
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm as UF
from django.views.decorators.http import require_POST

def profiles(r,u):
    u = get_object_or_404(User, username=u)
    is_owner = r.user == u
    return render(r, 'profiles.html',{"u" : u,'is_owner':is_owner})

def Chatbot(r):
    if r.method== 'GET':
        return render(r,'chatbot.html')
    if r.method == 'POST':
        d = r.data.get("message")
        chatbotmessage = chatbot(d)
        return render(r,'chatbot.html',{"message":chatbotmessage})

def login1_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')  # You'll need to add this field to the form

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'login1.html')

def Homepage(r):
    if r.method == "GET":
        g = Game.objects.all()
        s = S(g, many=True)
        return render(r, 'homepage.html',{"s":s})

'''def gd(s,r,id):
    if r.method == "GET":
        g = Game.objects.get(id=id)
        s = DS(g)
        return render()'''

def ll(r):
    if r.method == "GET":
        f = AF()
        return render(r, 'l.html', {"f": f})
    elif r.method == "POST":
        f = AF(data=r.POST)
        if f.is_valid():
            user = f.get_user()
            l(r, user)
            next_url = r.GET.get("next") or 'homepage'
            return redirect(next_url)

def llo(r):
    if r.method=="POST":
        lo(r)
        return redirect("homepage")
def signup(r):
    if r.method=='POST':
        f=CustomUserCreationForm(r.POST)
        if f.is_valid():
            u=f.save()
            l(r,u)
            return redirect('homepage')
        else:
            f=CustomUserCreationForm(r.POST)
            e="Error in form!"
            return render(r,'s.html', {"f":f,"e":e})
    else:
        f=CustomUserCreationForm()
        return render(r,'s.html', {"f":f})
def u(r):
    if r.method=='POST':
        f=CustomUserChangeForm(r.POST,instance=r.user)
        if f.is_valid():
            u=f.save()
            return redirect('profiles',u.username)
    if r.method=='GET':
        f=CustomUserChangeForm(instance=r.user)
        return render(r,'u.html',{"f":f})
def up(r):
    if r.method=='POST':
        f=CPF(r.POST,instance=r.user)
        if f.is_valid():
            u=f.save()
            return redirect('profiles',u.username)
    if r.method=='GET':
        f=CPF(instance=r.user)
        return render(r,'up.html',{"f":f})
@require_POST
def d(r):
    if r.user.is_authenticated:
        r.user.delete()
        lo(r)
        return redirect('homepage')