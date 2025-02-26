from django.urls import path
from . import views
urlpatterns = [
    path("",views.MList.as_view()),
    path('<int:id>/', views.MListD.as_view()),
]