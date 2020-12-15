from django.shortcuts import render

# # Create your views here.
from post.serializers import PostSerializer
from post.models import Post
from rest_framework import permissions ,viewsets

#REST IMPORTS 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import permissions ,viewsets
from rest_framework import generics

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
@api_view(['GET','POST'])
def post_list(request, format=None):
    """
    List all post or create new post
    """
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk,format=None):
    """
    List all post or create new post
    """
    try:
        posts = Post.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html',{ 'posts':posts})