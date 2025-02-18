from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post

from .serializers import PostSerializer

# Create your views here.
class PostListCreateView(APIView):
    def post(s, r):
        serializer = PostSerializer(data=r.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(s, r):
        o = Post.objects.all()
        serializer = PostSerializer(o, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class PostDetailView(APIView):
    def put(s, r, pk):
        d = r.data
        serializer = PostSerializer(Post.objects.get_or_404(id=pk), d)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({"message": "게시글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    def get(s, r, pk):
        serializer = PostSerializer(Post.objects.get_or_404(id=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)