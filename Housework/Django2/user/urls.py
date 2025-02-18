from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView

app_name = 'user'

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]