from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer, TaskListSerializer


class TaskListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).prefetch_related('changehistory_set')
# TODO swap to viewset
