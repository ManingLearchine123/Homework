from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
def signup(r):
    """회원가입"""
    f = UserCreationForm
    return r, "register.html", {'d':f}
def delete(r,pk):
    """사용자 삭제"""
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response({"message": "사용자가 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

class LoginAPIView(APIView):
    def post(self, request):
        """사용자 로그인 및 토큰 발급"""
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)  # 사용자 인증
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)  # 토큰 발급
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
class LogoutAPIView(APIView):
    def post(s,r):
        logout(request)
        return Response(status=status.HTTP_200_OK)

