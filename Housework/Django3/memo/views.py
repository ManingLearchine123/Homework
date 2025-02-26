from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Memo
from .serializers import MSerializer

# Create your views here.
class MList(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
    def get(s,r):
        o = Memo.objects.all()
        s=MSerializer(o, many=True)
        return Response(s.data, status=status.HTTP_200_OK)
    def post(s,r):
        s=MSerializer(data=r.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status = status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

class MListD(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticated(), IsUser()]
    def get(s,r,pk):
        m = get_object_or_404(Memo, pk=pk)
        s = MSerializer(m)
        return Response(s.data, status=status.HTTP_200_OK)
    def put(s,r,pk):
        m = get_object_or_404(Memo, pk=pk)
        d = r.data
        s = MSerializer(post, data=data, partial=True)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_200_OK)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(s,r,pk):
        m = get_object_or_404(Memo, pk=pk)
        post.delete()
        return Response({"message": "게시글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

