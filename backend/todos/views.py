# todos/views.py
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from .models import Todo
from .serializers import TodoSerializer


class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
