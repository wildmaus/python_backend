from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer, TaskListSerializer


class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.prefetch_related('statuschangehistory_set')
    serializer_class = TaskSerializer
