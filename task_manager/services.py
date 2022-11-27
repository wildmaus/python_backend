from .serializers import TaskInternalSerializer
from .models import ChangeHistory


def change_history(new_task, prev_task=None):
    changed = {}
    data = TaskInternalSerializer(new_task).data
    if prev_task:
        for field in data.keys():
            if getattr(prev_task, field) != getattr(new_task, field):
                changed[field] = data[field]
    else:
        changed = data
    if changed:
        ChangeHistory.objects.create(task=new_task, changed_to=changed)
