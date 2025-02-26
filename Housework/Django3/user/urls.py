from django.urls import path
from .views import LoginAPIView, signup,delete,LogoutAPIView
from . import views
from rest_framework.authtoken.views import obtain_auth_token  # DRF에서 제공하는 기본 토큰 발급 뷰

urlpatterns = [
    path('signup/', views.signup),
    path('delete/', views.delete),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # DRF 기본 제공 로그인 API -> 공식문서에서 요청을 어떤 형태로 보내야하는지 스터디 필요(get or post ..)
]