from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer


# Create your views here.
class UserListCreateAPIView(APIView):
    def post(self, request):
        """새로운 사용자 생성"""
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDetailAPIView(APIView):

    def delete(self, request, pk):
        """사용자 삭제"""
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({"message": "사용자가 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)