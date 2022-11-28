from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound

from .models import Task, ChangeHistory
from .serializers import TaskListSerializer, TaskSerializer, HistorySerializer


class TaskManagerPagination(PageNumberPagination):
    page_size = 5


class TaskListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer
    pagination_class = TaskManagerPagination

    def get_queryset(self):
        query = Q(user=self.request.user)
        if self.request.GET.get('status') and self.request.GET.get('status') in ('new', 'planned', 'in_work', 'done'):
            query = query & Q(status=self.request.GET.get('status'))
        if self.request.GET.get('date_end'):
            query = query & Q(date_end=self.request.GET.get('date_end'))

        if self.request.GET.get('order_by') and self.request.GET.get('order_by') in ('status', 'date_end', '-status', '-date_end'):
            return Task.objects.filter(query).order_by(self.request.GET.get('order_by'))
        return Task.objects.filter(query)


class TaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).prefetch_related('changehistory_set')


class HistoryView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = HistorySerializer
    pagination_class = TaskManagerPagination

    def get_queryset(self):
        queryset = ChangeHistory.objects.filter(
            Q(task__user=self.request.user) & Q(task__pk=self.kwargs['pk']))
        if queryset:
            return queryset
        else:
            raise NotFound()
