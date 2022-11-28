from rest_framework import serializers
from .models import Task, ChangeHistory


class TaskListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        exclude = ('date_created',)
        extra_kwargs = {
            'description': {'write_only': True}
        }


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    history = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_history(self, obj):
        return HistorySerializer(obj.changehistory_set.all()[:2], many=True).data


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeHistory
        fields = ('time', 'changed_to')


class TaskInternalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('user', 'id', 'date_created')
