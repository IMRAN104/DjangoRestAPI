from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from .models import Post
from .serializers import PostSerialier

# Create your views here.


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialier


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialier
