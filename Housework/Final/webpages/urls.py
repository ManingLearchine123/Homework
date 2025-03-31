from django.urls import path
from .views import Chatbot
from . import views
urlpatterns = [
    path('',views.Homepage, name='homepage'),
    path('chatbot/', views.Chatbot, name='chatbot'),
    path('login1/', views.login1_view, name='login1'),
    path("<str:u>",views.profiles, name="profiles"),
    path("u/", views.u,name='u'),
    path("up/", views.up,name='up'),
    path("login/", views.ll,name='l'),
    path("logout/", views.llo,name='lo'),
    path("signup/", views.signup, name='s'),
    path("d/",views.d,name='d'),


]