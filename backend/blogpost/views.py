from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from .models import Blogpost
from .serializers import BlogpostSerialier

# Create your views here.


class ListBlogpost(ListAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerialier


class DetailBlogpost(RetrieveAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerialier
