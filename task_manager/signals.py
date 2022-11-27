from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from .models import Task
from .services import change_history


@receiver(pre_save, sender=Task)
def task_pre_save(instance, **kwargs):
    if instance.pk is not None:
        prev = Task.objects.get(pk=instance.pk)
        change_history(instance, prev)


@receiver(post_save, sender=Task)
def task_post_save(instance, created, **kwargs):
    if created:
        change_history(instance)
