from rest_framework import serializers

from .models import Task, StatusChangeHistory


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_history(self, obj):
        return HistorySerializer(obj.statuschangehistory_set, many=True).data


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusChangeHistory
        fields = ('time', 'changed_to')
